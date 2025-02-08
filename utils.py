import os

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url


from dotenv import load_dotenv

load_dotenv()


def upload_image_to_cloudinary(image: str) -> str:
    """Upload an image to Cloudinary.

    Args:
        image (str | None, optional): Name of the image to be uploaded to cloudinary

    Returns:
        str: The URL of the uploaded image.
    """
    # Configuration       
    cloudinary.config( 
        cloud_name = f"{os.getenv('CLOUDINARY_CLOUD_NAME')}", 
        api_key = f"{os.getenv('CLOUDINARY_API_KEY')}", 
        api_secret = f"{os.getenv('CLOUDINARY_SECRET')}",
        secure=True
    )
    image_path = os.path.join(os.getcwd(), image) # Path to the image

    # Upload an image
    upload_result = cloudinary.uploader.upload(image_path,
                                            public_id="intruder_detected")
    return upload_result["secure_url"]