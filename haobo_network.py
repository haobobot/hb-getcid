import requests

class HBGetCid:
    """
    核心业务类
    优化：支持主备域名自动切换，初始化参数灵活配置
    """

    def __init__(self, uid=None, token=None, tid=None, tuser=None):
        # 初始化保持为空，支持后续动态赋值
        self.uid = uid
        self.token = token
        self.tid = tid
        self.tuser = tuser
        # 主备域名设置
        self.primary_url = "https://api.getcid.vip"
        self.backup_url = "https://api.f753.com"
        self.timeout = 25

    def _request_handler(self, endpoint, method="GET", params=None, data=None, files=None):
        """通用请求处理器，支持 GET 和 POST (OCR)"""
        urls = [self.primary_url, self.backup_url]
        last_error = None

        for base_url in urls:
            try:
                url = f"{base_url}/{endpoint}"
                if method == "GET":
                    response = requests.get(url, params=params, timeout=self.timeout)
                else:
                    response = requests.post(url, data=data, files=files, timeout=self.timeout)

                if response.status_code == 200:
                    try:
                        return response.json()
                    except:
                        return {"status": "success", "data": response.text}
            except Exception as e:
                last_error = str(e)
                continue
        return {"status": "error", "message": f"Connection failed: {last_error}"}

    def get_ocr(self, image_path=None, image_url=None, ocr_type="1", api_key=None):

        data = {
            "api": api_key or self.token,
            "type": ocr_type,
            "tid": self.tid,
            "tuser": self.tuser
        }

        if image_path:
            # 场景 1：上传本地图片
            with open(image_path, 'rb') as f:
                files = {'image': (image_path, f, "image/jpeg")}
                return self._request_handler("get_ocr", method="POST", data=data, files=files)
        elif image_url:
            # 场景 2：通过图片 URL 识别
            data["image_url"] = image_url
            return self._request_handler("get_ocr", method="POST", data=data)
        else:
            return {"status": "error", "message": "No image source provided"}

    def get_cid(self, iid, tid=None, token=None):
        """
        获取安装确认 ID (CID)
        优先级：函数参数 > 初始化参数
        """
        current_tid = tid or self.tid
        current_token = token or self.token

        if not current_token:
            return {"status": "error", "message": "Missing token"}

        params = {
            "iid": iid,
            "tid": current_tid,
            "token": current_token
        }
        return self._request_handler("api_get", params)

    def check_key(self, key, tid=None, token=None):
        """
        检查激活密钥 (PID)
        """
        current_tid = tid or self.uid
        current_token = token or self.token

        params = {
            "key": key,
            "tid": current_tid,
            "token": current_token
        }
        return self._request_handler("api_pid", params)

    def check_balance(self, uid=None, token=None):
        """
        查询余额 (UID)
        """
        target_uid = uid or self.uid
        current_token = token or self.token

        params = {
            "uid": target_uid,
            "token": current_token
        }
        return self._request_handler("api_uid", params)




