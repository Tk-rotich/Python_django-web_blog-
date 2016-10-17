data={'ALEX':500,'JAMES':20500,'KINUTHIA':70000}
def calculate_tax(data):
        while True:
            try:
                loop_data = data.keys()
                for item in loop_data:
                    pay = data[item]
                    if pay <= 1000:
                        tax = 0 

                    elif pay in range(1001,10001):
                        data[item] = ((0 * 1000)+(0.1 * (pay - 1000)))

                    elif pay in range(10001,20201):
                        tax = ((0 * 1000)+(0.1 * 9000)+(0.15 * (pay - 1000)))

                    elif pay in range(20201,30751):
                        tax = ((0 * 1000)+(0.1 * 9000)+(0.15 * 10200)+(0.20 * (pay - 20200)))

                    elif pay in range(30751,50001):
                        tax = ((0 * 1000)+(0.1 * 9000)+(0.15 * 10200)+(0.20 * 10550)+(0.25 * (pay - 30750)))

                    elif pay > 50000:
                        tax = ((0 * 1000)+(0.1 * 9000)+(0.15 * 10200)+(0.20 * 10550)+(0.25 * 19250)+(0.3 * (pay - 50000)))
                        data[item] = int(tax)
                return data
                break
                for key, value in data.items():
                    print(key,value)
            except (AttributeError,TypeError):
                raise ValueError('Input Error!!!!!')
             
            calculate_tax(data)
            
