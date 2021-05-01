#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2020--  
'''
import logging
class getLogger():
    def textlogger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formater = logging.Formatter('%(asctime)s - %(levelname)s-%(message)s')
        filepath = "log.log"
        filehander = logging.FileHandler(filepath)
        filehander.setLevel(logging.INFO)
        filehander.setFormatter(formater)
        self.logger.addHandler(filehander)
    def logINFO(self,INFO):
        self.logger.info(INFO)
        pass

    def logERROR(self,ERROR):
        self.logger.error(ERROR)
        pass

if __name__ == '__main__':
    g = getLogger()
    b = g.textlogger()
    g.logINFO("这是...级别")
