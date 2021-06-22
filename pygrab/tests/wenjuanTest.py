

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import time

url = 'https://www.wenjuan.com/s/UZBZJv0p4P/#'
t = 1


def commit_wenjuan():
    # 设置提交问卷次数
    global checkbox_answers, circleselect, options

    for times in range(t):
        driver = webdriver.Chrome()
        # 'https://www.wenjuan.com/s/UZBZJv0p4P/#'
        driver.get(url)

        # 定位所有的问卷问题
        questions = driver.find_elements_by_class_name("wjques")
        if len(questions) == 0:
            print("Empty question list. Exit")
            time.sleep(3)
            driver.quit()
            return None
        else:
            print("Got %s questions, processing start" % len(questions))

        for que in questions:
            print("Current question is %s" % que)
            if que is not None:
                # 定位所有问卷问题标题, 未找到内容进行next
                try:
                    answer_title = que.find_element_by_class_name("title")
                except Exception as err:
                    print("No answer_title in %s" % que)

                try:
                    blank_potion = que.find_element_by_class_name('blank-placeholder')
                except Exception as err:
                    print("No blank_potion in %s" % que)

                try:
                    checkbox_answers = que.find_elements_by_class_name('icheckbox_div')
                    for a in checkbox_answers:
                        print(a.text)
                    have_checkbox = True
                except Exception as err:
                    have_checkbox = False
                    print("No check_box in %s, %s" % que, err)

                try:
                    circleselect = que.find_element_by_tag_name("select")
                    options = que.find_elements_by_tag_name("option")
                    have_selectbox = True
                except Exception as err:
                    have_selectbox = False
                    print("No selectbox in %s" % que)

                # 定位需要填写文字的问题，并填入相关内容（有限覆盖范围内）
                if answer_title.text.find('姓名') != -1:
                    blank_potion.send_keys('李悦怡')
                if answer_title.text.find('手机') != -1:
                    blank_potion.send_keys('15738863312')
                if answer_title.text.find('身份证') != -1:
                    blank_potion.send_keys('410106199503120049')
                if answer_title.text.find('性别') != -1:
                    if have_checkbox:
                        try:
                            # checkbox_answers = que.find_elements_by_css_selector('.icheckbox_div')
                            for ans in checkbox_answers:
                                label = ans.find_element_by_css_selector('.option_label_wrap')
                                if label.text == '女':
                                    ans.click()
                        except Exception as err:
                            print("No fit option in %s" % que)
                    # if have_selectbox:
                    #     cho = 0
                    #     try:
                    #         for ops in options:
                    #             if ops.text == '女':
                    #                 cho = ops.value_of_css_property('data-index')
                    #                 print(cho)
                    #         Select(circleselect).select_by_index(cho)
                    #     except Exception as err:
                    #         print("No fit option in %s, %s" % (que, err))
            else:
                continue

            # choose_ans = random.choice(answer)
            # choose_ans.click()
        # time.sleep(2)
        subumit_button = driver.find_element_by_css_selector('#next_button')
        # subumit_button.click()
        print('已经成功提交了{}次问卷'.format(int(times)+int(1)))
        # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    commit_wenjuan()
