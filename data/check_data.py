import pandas as pd

def check_nan_in_files(x_train_path, x_val_path, x_test_path):
    files = {
        "X_train.csv": x_train_path,
        "X_val.csv": x_val_path,
        "X_test.csv": x_test_path
    }
    
    print("==================================================")
    print("   BÁO CÁO KIỂM TRA GIÁ TRỊ KHUYẾT (NAN) TRONG X  ")
    print("==================================================")
    
    for name, path in files.items():
        try:
            # Đọc file CSV
            df = pd.read_csv(path)
            
            # Đếm tổng số lượng NaN trong toàn bộ file
            total_nan = df.isnull().sum().sum()
            
            print(f"\n📁 File: {name}")
            print(f"   - Kích thước cấu trúc (Rows x Columns): {df.shape}")
            print(f"   - Tổng số ô bị khuyết (NaN): {total_nan}")
            
            # Nếu có lỗi NaN, in chi tiết từng cột bị dính
            if total_nan > 0:
                print("   - Chi tiết các cột chứa NaN:")
                nan_by_column = df.isnull().sum()
                for col, count in nan_by_column.items():
                    if count > 0:
                        percentage = (count / len(df)) * 100
                        print(f"     + Cột [{col}]: {count} dòng bị khuyết ({percentage:.2f}%)")
            else:
                print("   - Sạch sẽ! Không có cột nào bị khuyết.")
                
        except FileNotFoundError:
            print(f"\n❌ Không tìm thấy file: {name} tại đường dẫn đã cấu hình.")
        except Exception as e:
            print(f"\n❌ Lỗi khi đọc file {name}: {str(e)}")
            
    print("\n==================================================")

if __name__ == "__main__":
    # Cấu hình các đường dẫn tuyệt đối đến file của bạn ở đây
    X_TRAIN_PATH = r"C:\Users\This MC\nghi\uth\ml\e4\data\X_train.csv"
    X_VAL_PATH   = r"C:\Users\This MC\nghi\uth\ml\e4\data\X_val.csv"
    X_TEST_PATH  = r"C:\Users\This MC\nghi\uth\ml\e4\data\X_test.csv"
    
    check_nan_in_files(X_TRAIN_PATH, X_VAL_PATH, X_TEST_PATH)