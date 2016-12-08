def filter_by_foreign_fields(model_manager, **filter_fields):

    def filter_condition(model):

        if not hasattr(model, 'user'):
            return False

        model_fields = model.__dict__.items()
        user_fields = model.user.__dict__.items()

        # merge model and user field dicts
        fields = dict(model_fields + user_fields +
                      [(k, model_fields[k] + user_fields[k])
                       for k in set(model_fields) & set(user_fields)])

        for arg_name, arg_value in filter_fields.items():
            if arg_name not in fields:
                continue

            if arg_value != fields[arg_name]:
                return False

        return True

    return list(filter(filter_condition, model_manager.all()))
