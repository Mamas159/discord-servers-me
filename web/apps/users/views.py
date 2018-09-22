from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone
from web.apps.servers.models import DiscordServer


class UserDashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'dashboard.html'
    model = DiscordServer
    context_object_name = 'servers'
    paginate_by = 6

    def get_queryset(self):
        servers = DiscordServer.objects.filter(managers__manager_id=self.request.user.user_id).order_by('-bumped_at')
        return servers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot_invite_link'] = settings.DISCORD_BOT_INVITE_LINK
        context['show_bump_button'] = True
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.user.is_authenticated:
                sid = request.POST.get('sid')
                try:
                    server_obj = DiscordServer.objects.get(server_id=sid)
                except DiscordServer.DoesNotExist:
                    return JsonResponse({'error': 'Server does not exist.'})

                if server_obj.is_bumped():
                    return JsonResponse({'error': 'Server already bumped within 30 minutes.'})

                else:
                    server_obj.bumped_at = timezone.now()
                    server_obj.save()
                    return JsonResponse({'success': 'Server successfully bumped. Refresh to see changes.'})
            else:
                return JsonResponse({'error': 'User unauthenticated.'})
        else:
            return JsonResponse({'error': 'Invalid request.'})
