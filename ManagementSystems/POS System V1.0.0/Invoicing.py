import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import tkinter.font as font
import sqlite3


class InvoiceWindow:
    def __init__(self, master):
        self.tag = 'gray'
        self.master = master
        self.frame = tk.Frame(self.master)
        self.create_widgets()
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('.', font=('Helvetica', 10))

    def create_widgets(self):
        # create font for title
        title_font = font.Font(family='Helvetica', size=18, weight='bold')

        # create title label
        tk.Label(self.frame, text='Invoice', font=title_font).pack(side=tk.TOP, pady=10)
        # create frame for customer information
        customer_frame = tk.Frame(self.frame)
        tk.Label(customer_frame, text='Customer Name:').pack(side=tk.LEFT, padx=5, pady=5)
        self.customer_name_entry = ttk.Entry(customer_frame, width=30)
        self.customer_name_entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(customer_frame, text='Item Name:').pack(side=tk.LEFT, padx=5, pady=5)
        self.item_name_entry = ttk.Entry(customer_frame, width=30)
        self.item_name_entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(customer_frame, text='Quantity:').pack(side=tk.LEFT, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(customer_frame, width=30)
        self.quantity_entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(customer_frame, text='Price:').pack(side=tk.LEFT, padx=5, pady=5)
        self.price_entry = ttk.Entry(customer_frame, width=30)
        self.price_entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(customer_frame, text='Invoice Date:').pack(side=tk.LEFT, padx=5, pady=5)
        self.invoice_date_entry = ttk.Entry(customer_frame, width=20)
        self.invoice_date_entry.pack(side=tk.LEFT, padx=5, pady=5)
        customer_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        # create treeview widget to display invoice items
        self.tree = ttk.Treeview(self.frame, columns=('Quantity', 'Price', 'Total'))
        self.tree.heading('#0', text='Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Total', text='Total')
        self.tree.column('#0', width=200, stretch=tk.NO)

        self.tree.tag_configure('gray', background='#cccccc')
        # self.tree.tag_configure('gray', background='#CC9999')
        self.tree.tag_configure('light', background='#9999CC')

        self.tree.pack()

        # create frame for invoice totals
        totals_frame = tk.Frame(self.frame)
        tk.Label(totals_frame, text='Subtotal:').pack(side=tk.LEFT, padx=5, pady=5)
        self.subtotal_label = tk.Label(totals_frame, text='$0.00')
        self.subtotal_label.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Label(totals_frame, text='Tax:').pack(side=tk.LEFT, padx=5, pady=5)
        self.tax_label = tk.Label(totals_frame, text='$0.00')
        self.tax_label.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Label(totals_frame, text='Total:').pack(side=tk.LEFT, padx=5, pady=5)
        self.total_label = tk.Label(totals_frame, text='$0.00', font=title_font)
        self.total_label.pack(side=tk.LEFT, padx=5, pady=5)
        totals_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # create buttons
        ttk.Button(self.frame, text='Add Item', command=self.add_item).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.frame, text='Edit Item', command=self.edit_item).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.frame, text='Delete Item', command=self.delete_item).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(self.frame, text='Print Invoice', command=self.print_invoice).pack(side=tk.RIGHT, padx=5, pady=5)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def add_item(self):
        # add new item to invoice
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if not all([item_name, quantity, price]):
            messagebox.showerror('Error', 'Please enter all fields')
            return
        if not quantity.isdigit() or not price.isdigit():
            messagebox.showerror('Error', 'Quantity and price must be numeric')
            return
        if self.tag == 'light':
            self.tag = 'gray'
        else:
            self.tag = 'light'
        self.tree.insert('', 'end', text=item_name, values=(quantity, price, int(quantity) * float(price)),
                         tag=self.tag)
        self.clear_entry_fields()
        self.update_totals()

    def edit_item(self):
        # edit selected item in invoice
        item_id = 1

    def update_totals(self):
        # update subtotal, tax, and total labels
        subtotal = 0
        for child in self.tree.get_children():
            subtotal += float(self.tree.item(child)['values'][2])
        self.subtotal_label.configure(text=f'${subtotal:.2f}')
        self.tax_label.configure(text=f'${subtotal * 0.08:.2f}')

    def clear_entry_fields(self):
        # self.item_name_entry.delete(0, 'end')
        # self.quantity_entry.delete(0, 'end')
        # self.price_entry.delete(0, 'end')
        pass

    def delete_item(self):
        pass

    def print_invoice(self):
        # print invoice to printer
        printer_name = filedialog.askopenfilename(title='Select Printer', filetypes=[('Printer', '*.printer')])
        if not printer_name:
            return
            # connect to printer and print invoice
        conn = sqlite3.connect(printer_name)
        c = conn.cursor()
        c.execute('PRINT INVOICE')
        conn.commit()
        tk.messagebox.showinfo('Success', 'Invoice Printed')


def main():
    root = tk.Tk()
    root.title("Invoice")
    app = InvoiceWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
