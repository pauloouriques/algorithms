import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
print locale.currency(188518982.18, grouping=True)

print '{:,.2f}'.format(181616.0)