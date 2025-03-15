import os
import importlib
import logging

logger = logging.getLogger(__name__)

class PluginLoader:
    @staticmethod
    def load_plugins(command_manager, plugin_dir="plugins"):
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)
            logger.info(f"Created plugin directory: {plugin_dir}")
            return

        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f"{plugin_dir}.{module_name}")
                    if hasattr(module, "register"):
                        module.register(command_manager)
                        logger.info(f"Loaded plugin: {module_name}")
                except Exception as e:
                    logger.error(f"Failed to load plugin {module_name}: {str(e)}")