import pandas
from collections import defaultdict
from fugle_realtime import intraday

class Func:
       
    
    def __init__(self):
        data = pandas.read_csv('C:/Users/vanik/0319_ntu_scu/fugle_telegram_chatbot/symbol_info.csv', encoding = 'big5')
        data = data.drop(index=[203])
        dic = defaultdict(list)

        for indu, symbol in zip(data['industry'], data['symbol_id']):
            dic[indu].append(symbol)
        self.data = dic
        self.symbol_list = set(data['symbol_id'])
        self.api_token = 'c3a0ff515e0d1d65f2dabfc76d6750e1'
        self.symbol_id = None
        
    def maim(self, text):
        if text == '產業查股':
            reply = '請任選一個產業\n {}'.format(self.data.keys())
            return reply
        elif text in self.data.keys():
            reply = '下列是 {} 的股票代碼\n{}'.format(text, self.data[text])
            return reply
        elif text == '股票代碼查詢':
            reply = '請輸入欲查詢的股票代碼'
            return reply
        elif text in self.symbol_list:
            self.symbol_id = text
            reply = '請輸入【股票資訊】或【最佳五檔】'
            return reply
        elif text == '股票資訊':
            if self.symbol_id == None:
                reply = '要先輸入股票代碼唷！'
                return reply
            
            reply = self._get_meta(self.symbol_id)
            return reply
        elif text == '最佳五檔':
            if self.symbol_id == None:
                reply = '要先輸入股票代碼唷！'
                return reply
            
            reply = self._get_best_five(self.symbol_id)
            return reply
        else:
            reply = '輸入錯誤，請重新輸入'
            return reply
        

    def _get_meta(self, symbol_id):
        meta = intraday.meta(apiToken=self.api_token, symbolId=symbol_id)
        reply = '此為【' + meta['nameZhTw'][0] + '】的基本資訊\n'\
                '◆ 股票代碼：' + symbol_id + '\n'\
                '◆ 交易幣別代號：' + meta['currency'][0] + '\n'\
                '◆ 股票類型：' + meta['typeZhTw'][0] + '\n'\
                '◆ 是否為指數：' + str(meta['isIndex'][0]) + '\n'\
                '◆ 開盤參考價：' + str(meta['priceReference'][0]) + '\n'\
                '◆ 漲停價：' + str(meta['priceHighLimit'][0]) + '\n'\
                '◆ 跌停價：' + str(meta['priceLowLimit'][0])
        return reply
    
    def _get_best_five(self, symbol_id):
        quote = intraday.quote(apiToken=self.api_token, symbolId=symbol_id)
        reply = '此為【' + symbol_id + '】的最佳五檔\n'\
                '◆ bestAsks：\n'\
                '價格：' +  str(quote['order.bestAsks'][0][0]['price']) + '  張數：' + str(quote['order.bestAsks'][0][0]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestAsks'][0][1]['price']) + '  張數：' + str(quote['order.bestAsks'][0][1]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestAsks'][0][2]['price']) + '  張數：' + str(quote['order.bestAsks'][0][2]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestAsks'][0][3]['price']) + '  張數：' + str(quote['order.bestAsks'][0][3]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestAsks'][0][4]['price']) + '  張數：' + str(quote['order.bestAsks'][0][4]['unit']) + '\n'\
                '◆ bestBids：\n'\
                '價格：' +  str(quote['order.bestBids'][0][0]['price']) + '  張數：' + str(quote['order.bestBids'][0][0]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestBids'][0][1]['price']) + '  張數：' + str(quote['order.bestBids'][0][1]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestBids'][0][2]['price']) + '  張數：' + str(quote['order.bestBids'][0][2]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestBids'][0][3]['price']) + '  張數：' + str(quote['order.bestBids'][0][3]['unit']) + '\n'\
                '價格：' +  str(quote['order.bestBids'][0][4]['price']) + '  張數：' + str(quote['order.bestBids'][0][4]['unit']) + '\n'
        return reply