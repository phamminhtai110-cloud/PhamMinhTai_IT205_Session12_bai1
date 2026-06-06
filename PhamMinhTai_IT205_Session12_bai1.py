# Dữ liệu giỏ hàng (list chứa dict)
cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000}
]

while True:
    print("\n" + "="*50)
    print("SHOPEE CART MANAGEMENT SYSTEM")
    print("[1] Xem giỏ hàng")
    print("[2] Thêm sản phẩm / Cộng dồn")
    print("[3] Cập nhật số lượng")
    print("[4] Xóa sản phẩm")
    print("[5] Thoát")
    choice = input("Chọn (1-5): ").strip()

    # --- Chức năng 1: Xem giỏ hàng ---
    if choice == "1":
        if not cart_items:
            print("Giỏ hàng trống.")
        else:
            print("\nSTT | Mã SP | Tên SP               | SL | Đơn giá      | Thành tiền")
            total_qty = 0
            total_money = 0
            for i, item in enumerate(cart_items, 1):
                thanh_tien = item["number"] * item["price"]
                total_qty += item["number"]
                total_money += thanh_tien
                print(f"{i:<3} | {item['id']:<5} | {item['name']:<20} | {item['number']:<2} | {item['price']:>10,}đ | {thanh_tien:>10,}đ")
            print(f"\nTổng số lượng: {total_qty}")
            print(f"Tổng tiền: {total_money:,}đ")

    # --- Chức năng 2: Thêm sản phẩm ---
    elif choice == "2":
        pid = input("Mã sản phẩm: ").strip()
        name = input("Tên sản phẩm: ").strip()
        try:
            so_luong = int(input("Số lượng: "))
            don_gia = float(input("Đơn giá: "))
            if so_luong <= 0 or don_gia < 0:
                print("Lỗi: Số lượng phải > 0 và đơn giá >= 0")
                continue
        except:
            print("Lỗi: Nhập số hợp lệ")
            continue

        # Tìm sản phẩm theo mã
        tim_thay = False
        for item in cart_items:
            if item["id"] == pid:
                item["number"] += so_luong
                print(f"Cộng dồn thành công. Số lượng mới: {item['number']}")
                tim_thay = True
                break
        if not tim_thay:
            cart_items.append({"id": pid, "name": name, "number": so_luong, "price": don_gia})
            print("Thêm sản phẩm mới thành công.")

    # --- Chức năng 3: Cập nhật số lượng ---
    elif choice == "3":
        pid = input("Mã sản phẩm cần cập nhật: ").strip()
        try:
            sl_moi = int(input("Số lượng mới: "))
            if sl_moi <= 0:
                print("Số lượng phải lớn hơn 0")
                continue
        except:
            print("Số lượng phải là số nguyên")
            continue

        tim_thay = False
        for item in cart_items:
            if item["id"] == pid:
                item["number"] = sl_moi
                print(f"Cập nhật thành công. Số lượng mới: {sl_moi}")
                tim_thay = True
                break
        if not tim_thay:
            print("Mã sản phẩm không tồn tại.")

    # --- Chức năng 4: Xóa sản phẩm ---
    elif choice == "4":
        pid = input("Mã sản phẩm cần xóa: ").strip()
        vi_tri = -1
        for i, item in enumerate(cart_items):
            if item["id"] == pid:
                vi_tri = i
                break
        if vi_tri != -1:
            del cart_items[vi_tri]
            print("Xóa thành công.")
        else:
            print("Mã sản phẩm không tồn tại.")

    # --- Chức năng 5: Thoát ---
    elif choice == "5":
        print("Cảm ơn bạn! Tạm biệt.")
        break

    else:
        print("Lựa chọn không hợp lệ (1-5).")