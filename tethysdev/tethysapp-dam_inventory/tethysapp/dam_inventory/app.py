from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting

class DamInventory(TethysAppBase):
    """
    Tethys app class for Dam Inventory.
    """

    name = 'Dam Inventory'
    index = 'dam_inventory:home'
    icon = 'dam_inventory/images/icon.gif'
    package = 'dam_inventory'
    root_url = 'dam-inventory'
    color = '#15325e'
    description = 'A Tethys app created while doing the tutorial from docs.tethysplatform.org'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def custom_settings(self):
        """
        Example custom settings method.
        """
        custom_settings = (
            CustomSetting(
                name='max_dams',
                type=CustomSetting.TYPE_INTEGER,
                description='Maximum number of dams that can be created in the app.',
                required=False
            ),
        )
        return custom_settings

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='dam-inventory',
                controller='dam_inventory.controllers.home'
            ),
        )

        return url_maps