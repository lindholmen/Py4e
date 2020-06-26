import imageio, jieba
import wordcloud

# 1、准备文本数据
sentence = "这个阶段对我来说尤为重要，因为我了解到，技术上的能力固然重要，但和团队队员的沟通是一件更加重要的事情。往往有什么问题，需要讨论才能出结果；要做一个新feature，同样也要和相关的人一起沟通，才能制定出最佳解决方案；又如对于工作进度上的评估出错，像某段时间这个任务不能完成了，也需要和上级反应、沟通，才能保证项目计划和评估的正确不然到需要出结果的时候告诉别人这个东西做不出，这样的影响往往是很不好的。所以很多时候，技术不是主要问题，而在于团队协作和沟通。我想这也是柯达在招聘实习生的时候为什么看重这一点的原因。"

word = jieba.cut(sentence)
# 将返回的generator用空格拼接成字符串
words = " ".join(word)
# 输出分词后的结果
print(str)

# 2、生成图片的nd-array，传入图片路径
im = imageio.imread('engineer.png')

# 3. 颜色生成器
image_color = wordcloud.ImageColorGenerator(im)

# 4、创建词云对象
wc = wordcloud.WordCloud(width=2133,
                         height=2133,
                         background_color='white',
                         font_path='/Library/Fonts/Songti.ttc',
                         mask=im,
                         stopwords={"的","这个","往往","因为","才能","固然","来说"},
                         contour_width=1,
                         contour_color='black')

#wc_mask = np.array(Image.open(MASK_IMAGE))
# wordcloud = wordcloud.WordCloud(width=360,
#                        height=360,
#                        background_color="white",
#                        max_words=2000,
#                        mask = im,
#                        scale = 4,
#                        max_font_size=50,
#                        random_state=42,
#                        font_path="/Library/Fonts/msyh.ttc").generate(words)

    # # Display the generated image:
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()

# 5、通过文本数据生成词云
wc.generate(words)


# 6、保存词云文件
wc.to_file('wordcloud_output.png')

# 根据图片颜色重绘
# rwc = wordcloud.recolor(color_func=image_color)
# rwc.to_file('wordcloudw_repaint_output.png')

