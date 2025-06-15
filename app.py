from flask import Flask, render_template, request, jsonify
import joblib
import mysql.connector

app = Flask(__name__)

# Load các file ML
model = joblib.load('best_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')
le = joblib.load('label_encoder.pkl')

# Kết nối MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost', user='root', password='S=kblnwdat10042003', database='ml_predictor'
    )

@app.route('/predict', methods=['POST'])
def index():
    prediction = None
    # if request.method == 'POST':
    #     data = request.form

    #     text_input = (
    #         f"Tuổi: {data['age']} "
    #         f"Giới tính: {data['gender']} "
    #         f"Trình độ: {data['level']} "
    #         f"Cơ sở: {data['institution']} "
    #         f"Sinh viên CNTT: {data['isITStudent']} "
    #         f"Vị trí: {data['position']} "
    #         f"Tình trạng điện: {data['electricity']} "
    #         f"Tình trạng tài chính: {data['finance']} "
    #         f"Loại internet: {data['internetType']} "
    #         f"Loại mạng: {data['networkType']} "
    #         f"Thời lượng lớp: {data['classDuration']} "
    #         f"Hệ thống tự học: {data['selfLearning']} "
    #         f"Thiết bị: {data['device']}"
    #     )

    #     X_input = tfidf.transform([text_input])
    #     y_pred = model.predict(X_input)
    #     predicted_label = le.inverse_transform(y_pred)[0]

    #     # Lưu vào DB
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = """
    #         INSERT INTO predictions (
    #             age, gender, education_level, institution_type, it_student, location,
    #             load_shedding, financial_condition, internet_type, network_type,
    #             class_duration, self_lms, device, predicted_level
    #         )
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     """
    #     cursor.execute(sql, (
    #         data['age'], data['gender'], data['level'], data['institution'],
    #         data['isITStudent'], data['position'], data['electricity'],
    #         data['finance'], data['internetType'], data['networkType'],
    #         data['classDuration'], data['selfLearning'], data['device'], predicted_label
    #     ))
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    #     prediction = predicted_label

    return predicted_label


@app.route('/')
def inde2():
    return render_template('index.html')

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


