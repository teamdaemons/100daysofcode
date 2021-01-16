



def add(n1,n2):
  """Add two numbers"""
  return n1+n2

def subtract(n1,n2):
  """Subtracts two numbers"""
  return n1-n2

def multiply(n1,n2):
  """Multiply two numbers"""
  return n1*n2

def divide(n1,n2):
  """Divide two numbers"""
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = float(input("Whats your first number:"))
  for symbol in operations:
    print(symbol)
  decision="y"

  while decision:
    if decision!="n":
      operation_symbol= input("Pick an operation from the line above:")
      num2 = float(input("whats your second number:"))
      calculation_function = operations[operation_symbol]
      ans = calculation_function(num1,num2)
      print(f"{num1} {operation_symbol} {num2}: {calculation_function(num1,num2)}")
      num1=ans
      decision =input("Press y to continue n to stop")
    else:
      decision="n"
      calculator()
calculator()
# operation_symbol= input("Pick an operation from the line above:")
# num3 = int(input("whats your second number:"))

# calculation_function = operations[operation_symbol]

# print(f"{ans2} {operation_symbol} {num3}: {calculation_function(ans2,num3)}")




