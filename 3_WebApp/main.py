from flask import Flask, request, render_template
import settings
import utils
import numpy as np
import cv2
import predictions as pred

app = Flask(__name__)
app.secret_key = 'doucment_scanner_app'

docscan = utils.DocumentScan()


@app.route('/', methods=['GET', 'POST'])
def scandoc():
    if request.method == 'POST':
        file = request.files['image_name']
        upload_image_path = utils.save_upload_image(file)
        print('Image saved in = ', upload_image_path)

        four_points, size = docscan.document_scanner(upload_image_path)
        print(four_points, size)

        if four_points is None:
            message = 'UNABLE TO LOCATE THE COORDINATES OF DOCUMENT: points displayed are random'
            points = [
                {'x': 10, 'y': 10},
                {'x': 120, 'y': 10},
                {'x': 120, 'y': 120},
                {'x': 10, 'y': 120}
            ]
            return render_template('scanner.html',
                                   points=points,
                                   fileupload=True,
                                   message=message)
        else:
            points = utils.array_to_json_format(four_points)
            message = 'Located the Coordinates of Document using OpenCV. You can adjust them as per your convenience'
            return render_template('scanner.html',
                                   points=points,
                                   fileupload=True,
                                   message=message)

    return render_template('scanner.html')


@app.route('/transform', methods=['POST'])
def transform():
    try:
        points = request.json['data']
        array = np.array(points)
        magic_color = docscan.calibrate_to_original_size(array)

        filename = 'magic_color.jpg'
        magic_image_path = settings.join_path(settings.MEDIA_DIR, filename)
        cv2.imwrite(magic_image_path, magic_color)

        return 'success'
    except:
        return 'fail'


@app.route('/prediction')
def prediction():
    wrap_image_filepath = settings.join_path(settings.MEDIA_DIR, 'magic_color.jpg')
    image = cv2.imread(wrap_image_filepath)

    output_image, results = pred.getPredictions(image)
    output_image_filepath = settings.join_path(settings.MEDIA_DIR, 'output_image.jpg')
    cv2.imwrite(output_image_filepath, output_image)

    return render_template('predictions.html', results=results)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/help')
def help():
    return render_template('help.html')


# Run locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# For Gunicorn on Render
# Expose app instance to gunicorn
app = app
