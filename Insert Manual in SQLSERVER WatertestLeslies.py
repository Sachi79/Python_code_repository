import pyodbc
import sys
def image_to_binary(image_path):
    """
    Converts a JPG image to a binary object.

    Args:
        image_path (str): The path to the JPG image file.

    Returns:
        bytes: The binary representation of the JPG image, or None if an error occurs.
    """
    try:
        with open(image_path, 'rb') as image_file:
            binary_data = image_file.read()
            return binary_data
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#NoPhos_B_06-21-25
#Shock_B_06-21-25
#Tabs_B_06-21-25
# Example usage:
#C:\Projects\Leslie's\WaterTest\WaterTest_Image\Shock_B_06-21-25.jpg
#C:\Projects\Leslie's\WaterTest\WaterTest_Image\NoPhos_B_06-21-25.jpg
#C:\Projects\Leslie's\WaterTest\WaterTest_Image\Tabs_B_06-21-25.jpg
#NoPhos_B_06-21-25
#Shock_B_06-21-25
#Tabs_B_06-21-25

image_path = 'C:/Projects/Leslies/WaterTest/WaterTest_Image/Tabs_B_06-21-25.jpg'  # Replace with the actual path to your image file

# SQL Server connection details
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=watertest2-webdev.lesl.com;'
    'DATABASE=lwa3;'
    'UID=matillion;'
    'PWD=9o8i7u6y(O*I&U^Y;'
    'TrustServerCertificate=yes;'
    )
cursor = conn.cursor()

binary_image = image_to_binary(image_path)
print(sys.getsizeof(binary_image))

insert_sql = """
INSERT INTO Dynamic_Promos (
    SegmentID, CouponPrefix, CampaignID, PromotionID, DealID,
    StartDate, EndDate, Description, CouponImageArtwork,
    CouponImageExpiration, CreateDate, SegmentActive,
    UpdatedDate, UpdatedBy
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, GETDATE(), ?, GETDATE(), ?)
"""
cursor.execute(insert_sql, (
    'TB', 'R100001432', '2756', '2843', '19273',
    '2025-04-27 00:00:00.000', '2025-06-21 00:00:00.000', 'LPM - 25% Off - B - Leslie''s 3" Jumbo Tabs - 5 lb, 10 lb, 20 lb, or 35 lb - Limit 1, In Store Only',binary_image,
    sys.getsizeof(binary_image),
    True, 'matillion'
))

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully.")