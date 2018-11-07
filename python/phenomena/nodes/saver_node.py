# Author: Cristobal Pio
# Company: IFAE
# Date: 4 November 2018
# Mail: cgarcia@ifae.es
# Information: SaverNode will receive the information of each frame and will save it in
# a file

from abstract_node import Node


class SaverNode(Node):
    
    def __init__(self):
        Node.__init__(self, "Save")
    
    def configure(self, configure_message):
        pass

if __name__ == "__main__":
    a = SaverNode()