invoiceNumber = 0
cid = 0

class Customer:
    def __init__(self,customerName,mobile,email):
        self.customerName = customerName
        self.cid = cid
        cid += 1
        self.mobile = mobile
        self.email = email
        self.invoiceList  = []


class Invoice:
    def __init__(self,customerName , items , total ,cid):
        self.customerName = customerName
        self.invoiceNumber = invoiceNumber
        invoiceNumber += 1
        self.items = items
        self.total = total
        cid.invoiceList.append(self.invoiceNumber)

    def printInvoice(self):
        print "Customer Name : " + self.customerName 
        print "Invoice Number : " + self.invoiceNumber
        for i,v in self.items:
            print i + " \t " + v
        print "Total Cost : " + self.total

