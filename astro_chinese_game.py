print ('')
print ('WELCOME TO THE ASTRO CHINESE GAME')
print ('')
rat = [1888, 1900, 1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008,2020,2032,2044]
beef = [1889,1901, 1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021,2033, 2045]
tiger = [1890, 1902, 1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022, 2034, 2046]
hare = [1891, 1903, 1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023, 2035, 2047]
snake = [1893, 1905, 1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025, 2037, 2049]
goat = [1895, 1907, 1919, 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027, 2039, 2051]
rooster = [1897, 1909, 1921, 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029, 2041, 2053]
pig = [1899, 1911, 1923, 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031, 2043, 2055]
dragon = [1892, 1904, 1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024, 2036, 2048]
horse = [1894, 1906, 1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026, 2038, 2050]
monkey = [1896, 1908, 1920, 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028, 2040, 2052]
dog = [1898, 1910, 1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030, 2042, 2054]
name = raw_input('What is your name? : ')
print ('Hello ' +  name.upper() + ' Nice to meet you !!!')
print('')
chinese_sign = raw_input('Would you like to know your Astro Chinese Sign ? y/n : ')
if chinese_sign == 'y':
 birthday = raw_input ('OK !!! Enter your birthday year (example : 1902) :' )
 print('')
 if int(birthday) in dog:
 	print ('youre a DOG')
 elif int(birthday) in rat:
 	print ('youre a RAT')
 elif int(birthday) in beef:
 	print ('youre a BEEF')
 elif int(birthday) in tiger:
 	print ('youre a TIGER')
 elif int(birthday) in hare:
 	print ('youre a HARE')
 elif int(birthday) in snake:
 	print ('youre a SNAKE')
 elif int(birthday) in goat:
 	print ('youre a GOAT')
 elif int(birthday) in rooster:
 	print ('youre a ROOSTER')
 elif int(birthday) in pig:
 	print ('youre a DIRTY PIG')
 elif int(birthday) in dragon:
 	print ('youre a DRAGON')
 elif int(birthday) in horse:
 	print ('youre a HORSE')
 elif int(birthday) in monkey:
 	print ('youre a MONKEY')
 
if chinese_sign!= 'y':
 print ('OK Bye Bye')
print('')
print ('the end .... ')
