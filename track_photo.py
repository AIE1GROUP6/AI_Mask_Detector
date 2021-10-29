import argparse
import torch

def detectImage(args):
    source, output, yolo_weights_path = args.source, args.output, args.yolo_weights_path

    print('source : ' + source)
    print('output : ' + output)
    print('yolo_weights_path : ' + yolo_weights_path)

    if source == '':
        print('Usage : please enter image path -> "D:\\000.jpg"')
        return

    model = torch.hub.load('yolov5', 'custom', path=yolo_weights_path, source='local')  # local repo    

    results = model(source)
    
    results.show()
    try:
        results.save(output)
    except Exception as e:
        print(e)    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='', help='image path -> "D:\\000.jpg"')
    parser.add_argument('--output', type=str, default='output', help='output folder')
    parser.add_argument('--yolo_weights_path', type=str, default='yolov5\weights\mask.pt', help='model.pt path')
    args = parser.parse_args()
    
    detectImage(args)


