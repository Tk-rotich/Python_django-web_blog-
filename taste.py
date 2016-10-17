data={'Alex': 500,'James': 20500,'Kinuthia': 70000 } 
def calculate_tax('data'):
	
	for item in data:
		if item.values()>=0 and item.values()<=1000 :
			data[item]=(1000*0)

		elif item.values()>=1001 and item.values()<=10000 :
			data[item]=((1000*0)+(data[item]-1000)*0.1)

		elif item.values()>=10001 and item.values()<=20200 :
			data[item]=((1000*0)+(9000*0.1)+(data[item]-10000)*0.15)

		elif item.values()>=20201 and item.values()<=30750 :
			data[item]=((1000*0)+(9000*0.1)+(10200*0.15)+(data[item]-20200)*0.2)

		elif item.values()>=30751 and item.values()<=50000 :
			data[item]=((1000*0)+(9000*0.1)+(10200*0.15)+(10550*0.2)+(data[item]-307500)*0.25)

		elif item.values()>50000 :
			data[item]=((1000*0)+(9000*0.1)+(10200*0.15)+(10550*0.2)+(19250*0.25)+(data[item]-50000)*0.3)					

       
   
calculate_tax(data)