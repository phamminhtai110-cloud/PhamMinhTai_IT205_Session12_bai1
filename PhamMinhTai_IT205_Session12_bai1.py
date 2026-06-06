cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000}
]

def show_menu():
    print("\n====================================================")
    print("AMAZON CART MANAGEMENT SYSTEM")
    print("====================================================")
    print("1. Xem chi tiet gio hang & Tinh tong tien")
    print("2. Them san pham moi / Cong don so luong")
    print("3. Cap nhat so luong cua mot san pham")
    print("4. Xoa san pham khoi gio hang")
    print("5. Thoat chuong trinh")
    print("----------------------------------------------------")

def get_plate(prompt):  # thực chất là get_nonempty_string
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Loi: Khong duoc de trong!")
        else:
            return s

def get_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        if not s.isdigit():
            print("Loi: Vui long nhap so nguyen duong.")
            continue
        n = int(s)
        if n <= 0:
            print("Loi: So luong phai lon hon 0.")
            continue
        return n

def get_nonnegative_float(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Loi: Khong duoc de trong.")
            continue
        # kiem tra so thuc don gian: chi co chu so va toi da 1 dau cham
        valid = True
        dot_count = 0
        for ch in s:
            if ch == '.':
                dot_count += 1
                if dot_count > 1:
                    valid = False
                    break
            elif not ch.isdigit():
                valid = False
                break
        if not valid:
            print("Loi: Vui long nhap so (vi du: 15000 hoac 15000.5).")
            continue
        val = float(s)
        if val < 0:
            print("Loi: Don gia khong duoc am.")
            continue
        return val

def find_item(item_id):
    for item in cart_items:
        if item["id"] == item_id:
            return item
    return None

def display_cart():
    print("\n--- CHI TIET GIO HANG ---")
    if not cart_items:
        print("Gio hang trong.")
        return
    print(f"{'STT':<3} | {'MA SP':<6} | {'Ten San Pham':<25} | {'SL':<2} | {'Don Gia':>12} | {'Thanh tien':>12}")
    print("-" * 75)
    total_qty = 0
    total_money = 0
    for i, item in enumerate(cart_items, 1):
        thanh_tien = item["number"] * item["price"]
        total_qty += item["number"]
        total_money += thanh_tien
        print(f"{i:<3} | {item['id']:<6} | {item['name']:<25} | {item['number']:<2} | {item['price']:>11,}d | {thanh_tien:>11,}d")
    print("-" * 75)
    print(f"-> Tong so luong san pham trong gio: {total_qty}")
    print(f"-> TONG TIEN THANH TOAN: {total_money:,}d")

def add_product():
    print("\n--- THEM SAN PHAM MOI / CONG DON ---")
    product_id = get_plate("Nhap ma san pham: ").upper()
    product_name = get_plate("Nhap ten san pham: ")
    quantity = get_positive_int("Nhap so luong: ")
    price = get_nonnegative_float("Nhap don gia: ")
    # kiem tra ma ton tai
    item = find_item(product_id)
    if item is not None:
        item["number"] += quantity
        print(f"Da cong don. So luong moi cua {item['name']} la {item['number']}.")
    else:
        cart_items.append({
            "id": product_id,
            "name": product_name,
            "number": quantity,
            "price": price
        })
        print("Da them san pham moi vao gio hang.")

def update_quantity():
    print("\n--- CAP NHAT SO LUONG SAN PHAM ---")
    product_id = get_plate("Nhap ma san pham can cap nhat: ").upper()
    item = find_item(product_id)
    if item is None:
        print("Ma san pham khong ton tai trong gio hang.")
        return
    new_qty = get_positive_int("Nhap so luong moi: ")
    item["number"] = new_qty
    print(f"Da cap nhat so luong cua {item['name']} thanh {new_qty}.")

def remove_product():
    print("\n--- XOA SAN PHAM KHOI GIO HANG ---")
    product_id = get_plate("Nhap ma san pham can xoa: ").upper()
    for i, item in enumerate(cart_items):
        if item["id"] == product_id:
            del cart_items[i]
            print(f"Da xoa san pham {item['name']} khoi gio hang.")
            return
    print("Ma san pham khong ton tai trong gio hang.")

def main():
    while True:
        show_menu()
        choice = input("Nhap lua chon (1-5): ").strip()
        if not choice.isdigit() or int(choice) not in (1,2,3,4,5):
            print("Lua chon khong hop le. Vui long nhap so tu 1 den 5.")
            continue
        choice = int(choice)
        if choice == 1:
            display_cart()
        elif choice == 2:
            add_product()
        elif choice == 3:
            update_quantity()
        elif choice == 4:
            remove_product()
        elif choice == 5:
            print("\nCam on ban da su dung he thong. Tam biet!")
            break

if __name__ == "__main__":
    main()
