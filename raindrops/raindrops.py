def convert(number):
    raindrops = ''
    if number % 3 == 0:
        raindrops += 'Pling'
    if number % 5 == 0:
        raindrops += 'Plang'
    if number % 7 == 0:
        raindrops += 'Plong'
    raindrops = raindrops if raindrops else str(number)
    return raindrops
