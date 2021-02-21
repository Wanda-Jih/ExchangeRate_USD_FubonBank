import pandas
import time

def table():
    url='https://www.fubon.com/Fubon_Portal/banking/Personal/deposit/exchange_rate/exchange_rate1_photo.jsp?urlParameter=1D&currency=USD'
    dfs=pandas.read_html(url)
    currency=dfs[0] #table
    return currency

def show_buy_table(buy_price): #service=1
    temp=currency[0:1][['銀行賣出']].values
    if(temp<=buy_price):
        print('BUY USD NOW')
        print('The price is :',float(temp))
        print('\n')
    else:
        print('請再等等\n')

def show_sell_table(sell_price): #service=2      
    temp=currency[0:1][['銀行買入']].values
    if(temp>=sell_price):
        print('SELL USD NOW')
        print('The price is :',float(temp))
        print('\n')
    else:
        print('請再等等\n')
    
def service_costermus():
    tag=input('你要買美金(1))，還是要賣美金(2)\n')
    if(tag=='1'):
        service=1
        return service
    else:
        service=2
        return service
    
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec


if __name__ == '__main__':

    
    delaytime = sleeptime(0,1,0)
    
    while True:
        
        currency=table()
        print('目前的匯率')
        print(currency)
        service=service_costermus()
    
        # 買美金
        if(service==1): 
            buy_price=input('你希望買到的最低價格:\n')
            show_buy_table(float(buy_price))
                 
        # 賣美金   
        else:    
            sell_price=input('你希望賣出的價格高於:\n')
            show_sell_table(float(sell_price))
        print('############################')