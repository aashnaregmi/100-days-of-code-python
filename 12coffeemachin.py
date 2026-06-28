recources_needed={
  "espresso":{
         "water":50,
         "milk":0,
         "coffee":18,
         
    
  },
  "latte":{
         "water":200,
         "milk":150,
         "coffee":24,
         
    
  },
  "capaccino":{
         "water":250,
         "milk":100,
         "coffee":24,
    
  }
  
}

resources_available = {
    "water": 400,   
    "milk": 400,    
    "coffee": 100,  
    
}

coins={
  "quater":0.25,
  "dime":0.10,
  "nickel":0.05,
  "penny":0.01
  
}
def welcome_msg():
  print("=" * 45)
print("      ☕ WELCOME TO COFFEE MACHINE ☕")
print("=" * 45)

print("\nHello! What would you like today?\n")

print("📋 MENU")
print("-" * 45)
print("☕ Espresso      - $1.50")
print("🥛 Latte         - $2.50")
print("☕🥛 Cappuccino   - $3.00")
print("-" * 45)

print("\nCommands:")
print("• espresso")
print("• latte")
print("• cappuccino")
print("• report  - View machine resources")
print("• off     - Turn off the coffee machine")

print("=" * 45)
def check_resources(order):
  for key in resources_available:
    if recources_needed[order][key]>resources_available[key]:
        print(f"Sorry there is not enough {key}.")
        break
  else:
        return "enough"
    
def ask_coin():
    print("\nPlease insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))  

def process_order(order):
    resources_status=check_resources(order)
    if resources_status =="enough":
       ask_coin()
    
    

while True:
  welcome_msg()
  order=input("What is your order(Espresso,Latte,Cappuccino)?").lower()
  process_order(order)
  print("end")
  
 

  