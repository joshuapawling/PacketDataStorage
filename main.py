import encoder 
import keepalive

def main():
    keepalive.keep_alive()
    encoder.encode(f"ExampleVideo",f"video.mp4",.1,.1,30)

if __name__== "__main__":
    main()
