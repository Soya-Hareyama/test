from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView#①1行目でListViewクラスを読み込んでいます。ListViewは、データのリスト(今回であればGoodsに入っている商品のデータ)を便利に表示させるためのメソッドや属性が入っているクラスです。
from .models import Goods#②2行目でGoodsを読み込んでいます。
class GoodsList(ListView):#GoodsListクラスを作りました。ListViewを継承することで、ブラウザへの表示や使うデータベースを簡単に制御できます。
    model = Goods
    template_name = 'list.html'