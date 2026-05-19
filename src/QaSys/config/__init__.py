from QaSys import logger
from QaSys.entity import * 
from QaSys.utils import *
from QaSys.constants import *


class ConfigurationManager:

      def __init__(self, config = config, params = params):
            self.config = read_yaml(config)
            self.params = read_yaml(params)
            
            create_dir([self.config.root_artifact])
      
      

