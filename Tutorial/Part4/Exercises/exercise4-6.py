books = { '1578': 1, '1579': 2, '1580': 1, '1581': 2, '1582': 2, '1583': 3, '1584': 5, '1585': 1, '1586': 7, '1587': 4, '1588': 3, '1589': 4, '1593': 1, '1594': 2, '1595': 1, '1596': 1, '1597': 30, '1598': 91, '1599': 110, '1600': 163, '1601': 103, '1602': 91, '1603': 123, '1604': 117, '1605': 111, '1606': 31, '1607': 21, '1608': 24, '1609': 21, '1610': 11, '1611': 9, '1612': 9, '1613': 13, '1614': 13, '1615': 9, '1616': 28, '1617': 25, '1618': 30, '1619': 18, '1620': 12, '1621': 12, '1622': 12, '1623': 11, '1624': 16, '1625': 23, '1626': 36, '1627': 63, '1628': 47, '1629': 39, '1630': 53, '1631': 74, '1632': 51, '1633': 60, '1634': 60, '1635': 50, '1636': 49, '1637': 28, '1638': 54, '1639': 49, '1640': 67, '1641': 99, '1642': 117, '1643': 105, '1644': 105, '1645': 89, '1646': 100, '1647': 110, '1648': 114, '1649': 121, '1650': 106 }



import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

fig = plt.figure( figsize=( 12 , 4 ) )
ax = plt.axes()

ax.plot( books.keys() , books.values() , color = '#930d08' , linestyle = 'solid')

ax.set_xlabel('Year')
ax.set_ylabel('Annual production')

ax.set_title( 'STCN data')

plt.xticks(rotation=90)
plt.show()
