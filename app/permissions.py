from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_name = self.__get_model_permission_name(
            method=request.method,
            view=view,
        )

        if not model_permission_name:
            return False

        return request.user.has_perm(model_permission_name)

    def __get_model_permission_name(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_name}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view'
        }
        return method_actions.get(method, '')
