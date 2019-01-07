from aip import AipOcr
import json

class BaiduOcr():
    with open('keys/mypasswd.json') as f:
        mypasswd = json.load(f)
    APP_ID = mypasswd['APP_ID']
    API_KEY = mypasswd['API_KEY']
    SECRET_KEY = mypasswd['SECRET_KEY']

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    """ 调用通用文字识别, 图片参数为本地图片 获取原始结果 """
    def print_Results(self,filePath):
        image = self.get_file_content(filePath)
        result = self.client.basicGeneral(image)
        return result

    """ 获取文字结果 """
    def print_Text(self,filePath):
        content = self.print_Results(filePath)
        result = ""
        for c in content['words_result']:
            result += c['words']+'\n'
        print(result)
        return result

