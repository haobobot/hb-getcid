

#hb-getcid
pip install hb-getcid


# hb-getcid
# --- 灵活调用演示 ---
from hb_getcid import HBGetCid

if __name__ == "__main__":
    # 方式 1：初始化时一次性传入 (适合固定账号的机器人)
    client = HBGetCid(uid="you_id", token="you_token")
    print("方式 1 查询余额:", client.check_balance())

    # 方式 2：完全手动传参 (适合多租户/多用户场景)
    empty_client = HBGetCid(tid="you_id",token="you_token")
    res = empty_client.get_cid(
        iid="295190127616435381592726087454742312742251185119162781763744405",
    )
    print("方式 2 获取 CID:", res)


    # 方式 1：初始化时一次性传入 (适合固定账号的机器人)
    key_client = HBGetCid(uid="you_id", token="you_token")
    print("方式 1 查询密钥:", key_client.check_key("XMDMN-J34G2-3DKGT-PQVPX-7XQ4X"))


    #图片-OCR

    client_ocr = HBGetCid(token=" 你的_token",tid="你的用户_id",tuser="你的用户名_user")

    # Example 1: OCR with local file
    result_local = client_ocr.get_ocr(image_path="IMG_3243.jpeg")
    print("Local OCR:", result_local)

    # Example 2: OCR with image URL
    result_url = client_ocr.get_ocr(image_url="https://img.f753.com/photo.jpg")
    print("URL OCR:", result_url)


# --- Flexible Usage Examples ---

from hb_getcid import HBGetCid

if __name__ == "__main__":
    # Case 1: Initialize with fixed credentials
    # Best for: A dedicated Telegram Bot using a single administrative account.
    client = HBGetCid(uid="your_uid", token="your_token")
    print("Case 1 - Balance Inquiry:", client.check_balance())

    # Case 2: Dynamic parameters (Manual injection)
    # Best for: Multi-tenant scenarios where you handle requests for different TIDs.
    empty_client = HBGetCid(tid="your_tid", token="your_token")
    # Fetching Confirmation ID (CID) using a specific Installation ID (IID)
    res = empty_client.get_cid(
        iid="295190127616435381592726087454742312742251185119162781763744405"
    )
    print("Case 2 - Get CID Result:", res)

    # Case 3: Key Status Verification
    # Best for: Checking software product keys (PID)
    key_client = HBGetCid(uid="your_uid", token="your_token")
    key_result = key_client.check_key("XMDMN-J34G2-3DKGT-PQVPX-7XQ4X")
    print("Case 3 - Key Status Check:", key_result)


#imaget-OCR

    client_ocr = HBGetCid(token="you_token",tid="you_id",tuser="you_user")

    # Example 1: OCR with local file
    result_local = client_ocr.get_ocr(image_path="IMG_3243.jpeg")
    print("Local OCR:", result_local)

    # Example 2: OCR with image URL
    result_url = client_ocr.get_ocr(image_url="https://img.f753.com/photo.jpg")
    print("URL OCR:", result_url)


