from flask import Flask # type: ignore
from flask_cors import CORS, cross_origin # type: ignore
from flask import request #type: ignore
from flask import jsonify # type: ignore
from pytorch_tabnet.tab_model import TabNetClassifier
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo Flask Server Backennd
app = Flask(__name__)

#Apply Flask-CORS - cho phép domain khác gọi vào backend này
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

#loaded_model = TabNetClassifier()
#loaded_model.load_model("tabnet_model.zip.zip")
model = joblib.load(r"C:\Users\Administrator\Desktop\FinCare_MVP\FinCare_lỏ\tabnet_pipeline.pkl")
print(model)

#Khởi tạo các hàm
@app.route('/send_data', methods=['POST'])
def receive_name():
    data = request.get_json()
    feature_1 = int(data.get('feature_1'))
    feature_2 = int(data.get('feature_2'))
    feature_3 = int(data.get('feature_3'))
    feature_4 = int(data.get('feature_4'))
    feature_5 = int(data.get('feature_5'))
    feature_6 = int(data.get('feature_6'))
    feature_7 = int(data.get('feature_7'))
    feature_8 = int(data.get('feature_8'))
    feature_9 = int(data.get('feature_9'))
    feature_10 = int(data.get('feature_10'))
    feature_11 = int(data.get('feature_11'))
    feature_12 = int(data.get('feature_12'))
    feature_13 = int(data.get('feature_13'))
    feature_14 = int(data.get('feature_14'))
    feature_15 = int(data.get('feature_15'))
    feature_16 = int(data.get('feature_16'))
    new_data = np.array([[feature_1, 
                          feature_2, 
                          feature_3, 
                          feature_4, 
                          feature_5,
                          feature_6, 
                          feature_7, 
                          feature_8, 
                          feature_9, 
                          feature_10, 
                          feature_11, 
                          feature_12, 
                          feature_13, 
                          feature_14,
                          feature_15,
                          feature_15,
                          feature_15,
                          feature_15,
                          feature_15, 
                          ]])
    
    column = ['Tiền và các khoản tương đương tiền',
                'Đầu tư tài chính',
                'Các khoản phải thu',
                'Hàng tồn kho',
                'Tài sản cố định',
                'Bất động sản đầu tư',
                'XDCB dở dang',
                'Tài sản khác',
                'Nợ phải trả',
                'Vốn chủ sở hữu',
                'Doanh thu kế hoạch năm kế hoạch',
                'Lợi nhuận kế hoạch năm kế hoạch',
                'Tổng nhu cầu vốn',
                'Nguồn vốn cần vay',
                'Thời gian sử dụng hạn mức (năm)',
                'Khả năng thanh toán lãi vay',
                'Hiệu suất sử dụng tài sản ',
                'Hiệu suất sử dụng tài sản cố định',
                'Tỷ suất tự tài trợ']
    new_data = pd.DataFrame(new_data, columns=column)
    greeting = model.predict(new_data)

    model_1 = model.named_steps["model"]
    new_data = model.named_steps["preprocessor"].transform(new_data)

    masks = model_1.explain(new_data)[0][0]
    masks = masks.tolist()
    print(type(column), masks)
    
    # sorted_idx = np.argsort(feature_importance)[::-1]
    # sorted_features = [column[i] for i in sorted_idx]
    # sorted_importance = feature_importance[sorted_idx]
    # print(sorted_features)
    # print(sorted_importance)

    # # Lấy mask cuối cùng (độ quan trọng của feature trong quyết định cuối)
    #feature_importance = np.mean(masks[0], axis=0)  # Trung bình theo từng feature

    # # Vẽ biểu đồ
    # plt.figure(figsize=(10, 5))
    # plt.bar(column, feature_importance)
    # plt.xlabel("Feature")
    # plt.ylabel("Importance Score")
    # plt.title("Feature Importance in TabNet Prediction")
    # #plt.xticks(rotation=90)  
    # plt.xticks(rotation=40, ha='right')
    # plt.show()


    greeting = greeting.tolist()
    print(greeting)
    if greeting[0] == 0:
        greeting = "Hồ sơ không được chấp thuận"
    else:
        greeting = "Hồ sơ được chấp nhận"
    
    return jsonify({"message1": greeting, "label": column, "data_1": masks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)