class UserQuerySetMixin():

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data['author'] = self.request.user
        user = self.request.user
        if user.is_authenticated:
            return super().get_queryset().filter(**lookup_data)
        return super().get_queryset().filter(public=True)
