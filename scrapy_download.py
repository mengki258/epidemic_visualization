import requests

# 爬取数据并下载到本地数据库/云数据库

# 参考资料：https://lfengting.gitee.io/blog/2020/03/24/python%E7%88%AC%E8%99%AB%E5%AE%9E%E6%88%98

baidu_data= "https://voice.baidu.com/act/newpneumonia/newpneumonia/" # 百度开放接口，同理，可使用头条、腾讯新闻
domestic_trend = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish" #国内趋势
outland_trend = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish" #国外趋势
domestic_news="https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E8%82%BA%E7%82%8E" #国内新闻
outland_news = "https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E%E5%9B%BD%E5%A4%96%E7%96%AB%E6%83%85" #国外新闻

def get_outland_trend():
    res=requests.get(outland_trend)
    print(res.status_code)
    print(res.text)

def get_domestic_trend():
    res = requests.get(domestic_trend)
    print(res.status_code)
    print(res.text)

def get_domestic_news():
    res = requests.get(domestic_news)
    print(res.status_code)
    print(res.text)

def get_outland_news():
    res = requests.get(outland_news)
    print(res.status_code)
    print(res.text)

if __name__ == '__main__':
    # get_baidu_data()
    pass