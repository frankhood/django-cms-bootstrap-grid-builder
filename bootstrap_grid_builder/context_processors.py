from django.conf import settings


def grid_builder_settings(request):
    return {
        "grid_builder_attrs": {
            "BASE_STRUCTURE_TAG_TYPE_DIV": settings.BASE_STRUCTURE_TAG_TYPE_DIV,
            "BASE_STRUCTURE_TAG_TYPE_ARTICLE": settings.BASE_STRUCTURE_TAG_TYPE_ARTICLE,
            "BASE_STRUCTURE_TAG_TYPE_SECTION": settings.BASE_STRUCTURE_TAG_TYPE_SECTION,
            "BASE_STRUCTURE_TAG_TYPE_HEADER": settings.BASE_STRUCTURE_TAG_TYPE_HEADER,
            "BASE_STRUCTURE_TAG_TYPE_FOOTER": settings.BASE_STRUCTURE_TAG_TYPE_FOOTER,
            "BASE_STRUCTURE_TAG_TYPE_ASIDE": settings.BASE_STRUCTURE_TAG_TYPE_ASIDE,

            "VARIANT_GRID_CONTAINER_CLASS_NO_CONTAINER": settings.VARIANT_GRID_CONTAINER_CLASS_NO_CONTAINER,
            "VARIANT_GRID_CONTAINER_CLASS_BOXED": settings.VARIANT_GRID_CONTAINER_CLASS_BOXED,
            "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_SM": settings.VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_SM,
            "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_MD": settings.VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_MD,
            "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_LG": settings.VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_LG,
            "VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_XL": settings.VARIANT_GRID_CONTAINER_CLASS_FLUID_UNTIL_XL,
            "VARIANT_GRID_CONTAINER_CLASS_TOTALLY_FLUID": settings.VARIANT_GRID_CONTAINER_CLASS_TOTALLY_FLUID,

            "TAG_TYPE_GRID_CONTAINER_SECTION": settings.TAG_TYPE_GRID_CONTAINER_SECTION,
            "TAG_TYPE_GRID_CONTAINER_DIV": settings.TAG_TYPE_GRID_CONTAINER_DIV,

            "VARIANT_GRID_ROW_CLASS_LEFT": settings.VARIANT_GRID_ROW_CLASS_LEFT,
            "VARIANT_GRID_ROW_CLASS_CENTER": settings.VARIANT_GRID_ROW_CLASS_CENTER,
            "VARIANT_GRID_ROW_CLASS_RIGHT": settings.VARIANT_GRID_ROW_CLASS_RIGHT,
            "VARIANT_GRID_ROW_CLASS_AROUND": settings.VARIANT_GRID_ROW_CLASS_AROUND,
            "VARIANT_GRID_ROW_CLASS_BETWEEN": settings.VARIANT_GRID_ROW_CLASS_BETWEEN,
        }
    }