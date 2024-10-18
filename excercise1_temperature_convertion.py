if __name__ == "__main__":
  def convertToFarenheit(degCelsius):
    """This function converts the degCelsious value to its equivalent in Farenheit degrees"""
    return degCelsius * (9/5) + 32

  def convertToCelsius(degFar):
    """This function converts the degFar value to its equivalent in Celsius degrees"""
    return (degFar -32) * (5/9)


  print convertToCelsius(0)
  print convertToCelsius(180)
  print convertToFarenheit(0)
  print convertToFarenheit(100)
  print convertToCelsius(print convertToFarenheit(15))
