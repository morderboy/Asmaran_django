from django_select2.forms import ModelSelect2Widget


class CustomModelSelect2Widget(ModelSelect2Widget):
    def build_attrs(self, *args, **kwargs):
        # Устанавливаем минимальное количество символов для поиска на 0
        attrs = super().build_attrs(*args, **kwargs)
        attrs['data-minimum-input-length'] = 0  # Позволяет отображать все элементы при открытии
        return attrs