from text_config_based_file_extension_manager import TextConfigBasedFileExtensionManager


class FileExtensionManagerFactory:
    def __init__(self):
        self.custom_manager = None

    def create(self):
        if self.custom_manager is not None:
            return self.custom_manager
        return TextConfigBasedFileExtensionManager()


FILE_EXTENSION_MANAGER_FACTORY = FileExtensionManagerFactory()
