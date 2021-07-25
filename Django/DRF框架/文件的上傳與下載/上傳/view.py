class Uploadfile(View):
    def post(self, request):
        file = request.get("myfile", None)

        if file is None:
            return HttpResponse("沒有上傳的文件")
        else:
            with open(file.name, "wb+") as f:
                for chunk in file.chunks(): # 分塊寫入文件
                    f.write(chunk)

            return JsonResponse({"errmsg": "更新成功"})
