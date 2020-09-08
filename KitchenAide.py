import streamlit as st
import numpy as np
import pandas as pd
import pickle


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


# st.markdown('<div class="header"></div>', unsafe_allow_html=True)

local_css("style.css")

# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")

# Kitchen & You
# KitchenJr
# FoodImport
#'# ChefNest'
# MealByte

def showall(targets,df):
    if(len(targets)==0):
        return df
        
    elif(len(targets)==1):
        return df[df.Ingredients2.str.contains(targets[0])]
    else:
        init = df.Ingredients2.str.contains(targets[0]).to_numpy()
        for word in targets[1:]:
            result = df.Ingredients2.str.contains(word).to_numpy()
            ans = np.logical_and(init,result)
            init = ans
        return df[ans]


vocabnew=[
    'Salt/Namak','Water/Paani','Oil/Tel','Turmeric Powder/Haldi','Ginger/Adrak','Asafoetida/Hing',
    'Coriander Leaves/Dhania Patta','Cumin Seeds/Jeera','Curry Leaves/Kadhi Patta','Red Chilli Powder/Lal Mirch',
    'Green Chilli/Hari Mirch','Mustard Seeds/Rai','Onion/Pyaaz','Tomato/Tamatar','Lemon Juice/Lime Juice/Nimbu Ras','Cumin Powder/Jeera Powder',
    'Clove/Laung','Cinnamon/Dal Cheeni','Garlic/Lahsun','Green Cardamom/Choti Elaichi',
    'Coriander Powder/Dhania Powder','Coconut/Nariyal','Potato/Aloo','Indian Bay Leaf/Tej Patta','Cashew/Kaju','Red Chilli/Lal Mirch','Black Pepper Powder/Kaali Mirch Powder',
    'Baking Soda','Chaat Masala','Clarified Butter/Ghee','Chickpea Flour/Besan','Mint Leaves/Pudina Patta','Peanuts/Moong Fali','Wheat Flour/Atta',
    'Rice Flour/Chawal Atta','Carrot/Gajar','Coriander Seeds/Dhania Beej','Jaggery/Gur','Black Salt/Kala Namak','Coconut Oil/Nariyal Tel','Mango Powder/Amchur Powder','Saffron/Kesar',
    'Cardamom Powder/Elaichi Powder','Black Cardamom/Badi Elaichi','Carrom Seeds/Ajwain','Fennel Seeds/Saunf','Peas/Matar','Black Gram/Urad Dal','Basmati Rice/Basmati Chawal','Fenugreek Leaves/Kasuri Methi',
    'Cilantro Leaves/Dhania Patta','Tamarind/Imli','Sesame Seeds/Til','Mustard Oil/Sarso Tel','Beans/Gwar Fali','Mace/Javitri','Almond/Badam','Celery/Ajwain Patta','Cottage Cheese/Paneer','Milk/Doodh','Baking Powder','All Purpose Flour/Maida','Butter/Margarine/Makhan','Ice/Baraf',
    'Fenugreek Seeds/Methi','Curd/Yogurt/Dahi','Cream/Malai','Cabbage/Patta Gobi','Raisins/KishMish','Tapioca Pearls/Sabudana','Olive Oil','Soy Sauce','Sesame Oil/Til Tel','Cauliflower/Gobi','Bengal Gram/Chana Dal',
    'Rice/Chawal','Spring Onion/Hara Pyaaz','Garam Masala','Coconut Milk/Nariyal Doodh','Bread','Peanut Oil/Moong Fali Tel','Sambar Powder','Capsicum/Bell Pepper/Shimla Mirch','Mushroom','Dry Ginger Powder/Saunth','Nutmeg/Jaifal','Mango/Aam',
    'Black Peppercorns/Kali Mirch','Poppy Seeds/Khus Khus','Cucumber/Kheera/Kakdi','Mustard/Sarso','Pistachios/Pista','Lemon/Nimbu','Okra/LadyFinger/Bhindi','Ginger Garlic Paste','Sev','Spinach/Palak','Star Anise/Chakriphool',
    'Sugar/Cheeni','Tomato Puree','Banana/Kela','Oregano','Pigeon Pea Lentils/Arhar Dal/Tuvar Dal','Vegetable Stock','Green Gram/Moong Dal','Pomegranate/Anaar','Flattened Rice/Poha','Caraway Seeds/Shahi Jeera','Vanilla Extract','Baby Corn','Yeast','Corn Starch/Corn Flour',
    'Pomegranate Seeds/Anardana','Strawberry','Rose Water/Gulab Jal','Nigella Seeds/Kalonji','Vinegar/Sirka','Piece Stone Flower/Dagad Phool','Sunflower Oil','White Pepper/Safed Mirch','Basil Leaves/Tulsi',
    'Water Chestnut Flour/Paniphal Flour/Singhare Ka Atta','Green Chutney/Coriander Chutney','Buckwheat Flour/Kuttu Atta','Cheese','Dates/Khajoor','Walnut/Akhrot','Tomato Ketchup/Sauce','Bread Crumbs','Corn/Makki','Beetroot/Beets/Chukandar','Dill Leaves/Savaa Patta','Pumpkin/Kaddu','Rose Syrup','Yam/Jimikand/Suran/Garadu',
    'Sunflower Seeds/Surajmukhi Beej','Kapok Buds/Marathi Moggu','Kokum','Galangal/Kulanjan','Sweet Potatoes/Shakarkandi','Indian Gooseberry/Amla','Ash Gourd/Petha','Pav Bhaji Masala','Puffed Rice/Murmura','Red Chilli Flakes','Rose Petals/Gulab','Colocasia Leaves/Arbi Patta','Idli Rice','Cocoa Powder',
    'Semolina/Rawa/Sooji','Apple/Seb','Noodles','Fruit Salt/Eno','Lettuce','Idli Batter/Uttapam Batter','Raw Banana','Sprouted Moong Beans/Sprouts','Lemon Grass','White Chickpeas/Chole/Kabuli Chana/Safed Chana','Turmeric Leaves','Papdis',
    'Papaya/Papita','Pineapple/Ananas','Black Chickpeas/Kala Chana','Amaranth Flour/Rajgira Atta','Camphor/Kapoor','Indian Five Spice/Panch Phoron','Orange Juice/Santra Ras','Tutti Frutti','Sichuan Pepper','Coconut Chutney','Bitter Gourd/Karela',
    'Pink Lentils/Masoor Dal','Schezwan Sauce','Almond Milk','Millet Flour/Bajra Flour','Fig/Anjeer','Dry Fruits','Finger Millet Flour/Ragi Flour','Buttermilk/Chaas','Kaffir Lime','Parsley','Barnyard Millet/Sama Ke Chawal','Arrow Root Flour',
    'Brinjal/Eggplant/Baingan','Melon Seeds/Magaz','White Cowpeas/Red Cowpeas/Lobia','Lilva Beans/Hyacinth Beans/Avrekaalu','Goda Masala/Kala Masala','Colocasia Roots/Arbi','Honey/Shahad','Milk Powder','Seeraga Samba Rice','Coffee','Orange/Santra',
    'Bottle Gourd/Opo Squash/Lauki/Dudhi','Sodium Benzoate','Radish/Mooli','Chenopodium/Bathua Leaves','Saag','Maize Flour/Makki Atta','Soy Milk','Custard Powder','Khoya/Mawa','Almond Meal/Almond Paste','Flax Seeds/San Beej','Soyabean','Burger Buns','Oats','Aam Panna',
    'Sorghum Flour/Jowar Flour','Foxnuts/Lotus Seeds/Makhana','Jalapeno','Raw Mango/Kairi/Kachcha Aam','Drumstick','Kidney Beans/Rajma','Guava/Amrood','Ivy Gourds/Tendli','Tofu','Avocado','Vermicelli','Akki Shavige','Sapota/Chickoo',
    'Sandalwood Powder','Boondi','Vangi Bath Masala Powder','Smoked Paprika','Sriracha Sauce','Broccoli','Watermelon/Tarbooz','Black Peas/Kala Vatana','Tea/Chai','Agar Agar','Bengal Quince/Stone Apple/Wood Apple/Bel Fruit','Mayonnaise','Snake Gourd/Padwal/Chichinda',
    'Blueberry','Pani Puris/Golgappa Puris','Cherry','Chia Seeds','Neem','Ridge Gourd/Turai','Idli Podi','Pav','Condensed Milk','Basil Seeds/Sabja','Jackfruit/Katahal','Pointed Gourds/Parwal','Bread Croutons','Broken Wheat/Dalia','Chocolate','Marshmallow','Biscuit','Papad','Chicken','Fish','Mutton','Crab','Egg/Anda','Chive','Chipotle','Cuddapah Almond/Chironji',
    'Lychee','Apricot','Peach','Zucchini/Courgette','Zatar','Squash','Worcestershire Sauce','Thai Curry Paste','Yellow Chilli','Wonton Wrapper','Pasta','Spaghetti','Pizza Base','White Wine','Quinoa','Grape/Grapes','Whiskey','Wasabi','Vodka','Gelatin','Turnip','Tuna','Tahini','Treacle','Tobasco Sauce','Prawn',
    'Thyme','Tequila','Chhole Masala','Meat Masala','Tarragon','Olives','Prunes','Star Fruit','Squid','Soy Bean','Soup Stick','Sour Dough Starter','Shrimp','Lamb','Sherry','Screwpine','Scallop','Sausage','Salsa','Salmon','Sake','Sage','Rum','Rosemary','Red Wine','Raspberry','Rasam Powder','Quail','Pork','Pomfret','Plum',
    'Pine Nuts/Chilgoza','Gherkin','Peri Peri Masala','Pear','Passion Fruit','Oyster Sauce','Oatmeal','Nihari Masala','Nachos','Mussels','Muskmelon','Mussallam Masala','Mulberry','Muesli','Moringa Leaves','Molasses','Gun Powder/Molgapodi','Jam','Lotus Stem','Long Pepper/Pipli','Lobseter','Leek','Green Chana',
    'Kiwi','Kale','Indian Blackberry/Jamun','HP Sauce','Hazelnut','Ham','Gum/Gond','Maple Syrup','Cranberry','Couscous','Clams','Sapota/Chikoo','Biryani Masala','Beer','Barley','Barbeque Sauce','Bacon','Asparagus','Artichoke','Aioli','Alfalfa','Bok Choy','Duck','Shallot','Tapioca Flour','Amaranth']




st.markdown(f'<h1 style="font-family:brush script mt;text-align:center;color:black;font-size:100px;font-weight: bold">KitchenAide</h1>',unsafe_allow_html=True) #aesthetic addition
st.markdown(f'<h3 style="font-weight: bold">What are we cooking today?</h3>',unsafe_allow_html=True)
st.markdown(f'<div class="div1"><p style="font-family:garamond;font-size:18px;font-weight: bold">Select from the different options like Cuisine, amount of time you would like to spend and the ingredients you want to cook with, and Voila! Your everyday hassle of what to cook vanished!</p></div>',unsafe_allow_html=True)


# st.image("https://w7.pngwing.com/pngs/210/320/png-transparent-chef-graphics-graphic-design-cooking-cooking-vertebrate-cooking-cook.png",width=300)


df = pickle.load(open('db3.p','rb'))
options = st.sidebar.multiselect('Which type of food would you like?',df['Style'].unique())
# st.success('Hi guysssssssssssssssssssssssss')
# st.info('hehehe')
# st.balloons()
df1 = df[df['Style'].isin(options)].dropna()
second_ques=['Any','<30 mins','<1 hour','<3 hours']
options1 = st.sidebar.selectbox('How much time are you willing to spend?',second_ques)

if(options1=='Any'):
    df2=df1.copy()
elif(options1=='<30 mins'):
    df2=df1.where(df1['Time']<=30).dropna()
elif(options1=='<1 hour'):
    df2=df1.where(df1['Time']<=60).dropna()
elif(options1=='<3 hours'):
    df2=df1.where(df1['Time']<=180).dropna()
# st.write(df2['Dish'],height=2000)
third_ques=['World','Indian','All']
options2 = st.sidebar.selectbox('Which Cuisine?',sorted(third_ques))


if(options2=='All'):
    df3=df2.copy()
    lastoption=st.multiselect('Ingredients(Type In or Select from Dropdown)',vocabnew)
    ing=list(map(str.lower,lastoption))
    # finaldf=df3[df3['Ingredients2'].str.contains('|'.join(ing))]
    # st.write(finaldf.to_html(escape=False, index=False), unsafe_allow_html=True)
    # st.balloons()

    # includeAny = st.checkbox('Include Any Ingredient From Above')
    # includeAll = st.checkbox('Include All Ingredients')
    includeOptions = st.radio('',('Include Any Ingredient From Above','Include All Ingredients'))

    for i in range(len(ing)):
        ing[i]='|'.join(ing[i].split('/'))
    
    if(includeOptions == 'Include Any Ingredient From Above'):
        if(len(df3)!=0):
            finaldf=df3[df3['Ingredients2'].str.contains('|'.join(ing))]
            # st.write(finaldf[['Dish']].style.hide_index())

            finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
            # finaldf=finaldf.style.format({'nameurl': make_clickable_both})
            # finaldf = finaldf.reset_index()
            for i in range(len(finaldf)):
                name, url = finaldf.iloc[i]['nameurl'].split('#')
            # return f'<a href="{url}">{name}</a>'
                # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

                sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                # optionrecipe=st.selectbox('Recipes',finaldf.Dish.unique())
                # <a href="{url}">{name}</a>
            if(len(finaldf)==0):
                st.info('No recipes found')
    else:
        finaldf = showall(ing,df3)
        finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
        for i in range(len(finaldf)):
            name, url = finaldf.iloc[i]['nameurl'].split('#')
                # return f'<a href="{url}">{name}</a>'
                    # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

            sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
            st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
        # except:
        #     st.info('Select Ingredients First')
        if(len(finaldf)==0):
                st.info('No recipes found')

elif(options2=='World'):
    df3=df2.where(df2['Cuisine1']!='Indian' ).dropna()
    fourth_ques1=['All','African','American', 'British', 'Australian', 'Brazilian', 'Fusion', 'Burmese', 'Canadian', 'Carribean', 'Chinese', 'Continental',            
    'Cuban','Denmark','French','Italian','German','Greek','Indo Chinese','Indonesian','Malaysian','Thai','Irish','Spanish','Jamaican','Japanese',
    'Korean', 'Lebanese', 'Malaysian', 'Mexican', 'Middle Eastern', 'Mongolian', 'Moroccan', 'Pakistani', 'Parsi', 'Peruvian', 'Polish', 'Portuguese',
    'Rome','Russian','Scottish','Sindhi','Singaporean','South African','Sri Lankan','Swiss','Tibetian','Turkish','Viennese','Vietnamese']
    options3=st.sidebar.multiselect('Narrowing down your Cuisine',sorted(fourth_ques1))
    # df[df['A'].str.contains("hello")]
    if('All' in options3):
        df4=df3.copy()
    else:
        df4=df3[df3['Cuisine2'].str.contains('|'.join(options3))]
    lastoption=st.multiselect('Ingredients(Type In or Select from Dropdown)',vocabnew)
    ing=list(map(str.lower,lastoption))

    includeOptions = st.radio('',('Include Any Ingredient From Above','Include All Ingredients'))

    for i in range(len(ing)):
        ing[i]='|'.join(ing[i].split('/'))

    if(includeOptions == 'Include Any Ingredient From Above'):
        if(len(df4)!=0):
            finaldf=df4[df4['Ingredients2'].str.contains('|'.join(ing))]
            # st.write(finaldf[['Dish']].style.hide_index())

        finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
        # finaldf=finaldf.style.format({'nameurl': make_clickable_both})
        for i in range(len(finaldf)):
            name, url = finaldf.iloc[i]['nameurl'].split('#')
        # return f'<a href="{url}">{name}</a>'
            # st.markdown(f'<style>.button {{border: none;color: white; padding: 16px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}}.button1 {{background-color: white; color: black; border: 2px solid #602487;}}.button1:hover {{background-color: #602487;color: white;}}</style><a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
            sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
            st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
        # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
    # optionrecipe=st.selectbox('Recipes',finaldf.Dish.unique())
        if(len(finaldf)==0):
                st.info('No recipes found')
    else:
        finaldf = showall(ing,df4)
        finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
        for i in range(len(finaldf)):
            name, url = finaldf.iloc[i]['nameurl'].split('#')
                # return f'<a href="{url}">{name}</a>'
                    # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

            sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
            st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
        if(len(finaldf)==0):
                st.info('No recipes found')

else:
    df3=df2.where(df2['Cuisine1']!='World').dropna()
    fourth_ques2=['All','North','East','West','South','Street Food','Mughlai','Fusion']
    options3=st.sidebar.multiselect('Narrowing down your Cuisine',fourth_ques2)
    if('All' in options3):
        df4=df3.copy()
        lastoption=st.multiselect('Ingredients(Type In or Select from Dropdown)',vocabnew)
        ing=list(map(str.lower,lastoption))

        includeOptions = st.radio('',('Include Any Ingredient From Above','Include All Ingredients'))

        for i in range(len(ing)):
            ing[i]='|'.join(ing[i].split('/'))

        
        if(includeOptions == 'Include Any Ingredient From Above'):
            if(len(df4)!=0):
                finaldf=df4[df4['Ingredients2'].str.contains('|'.join(ing))]
                # st.write(finaldf[['Dish']].style.hide_index())

                finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
                # finaldf=finaldf.style.format({'nameurl': make_clickable_both})
                for i in range(len(finaldf)):
                    name, url = finaldf.iloc[i]['nameurl'].split('#')
                # return f'<a href="{url}">{name}</a>'
                    # st.markdown(f'<style>.button {{border: none;color: white; padding: 16px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}}.button1 {{background-color: white; color: black; border: 2px solid #602487;}}.button1:hover {{background-color: #602487;color: white;}}</style><a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
                    sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                    st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                if(len(finaldf)==0):
                    st.info('No recipes found')
            # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
        # st.write(df4)
        else:
            finaldf = showall(ing,df4)
            finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
            for i in range(len(finaldf)):
                name, url = finaldf.iloc[i]['nameurl'].split('#')
                    # return f'<a href="{url}">{name}</a>'
                        # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

                sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
            if(len(finaldf)==0):
                st.info('No recipes found')
    else:
        df4=df3[df3['Cuisine2'].str.contains('|'.join(options3))]

    
        fifth_ques_n=['All', 'Punjabi', 'Uttar Pradesh', 'Kashmiri', 'Rajasthani','Bihari', 'Banarasi', 'Awadhi', 'Jammu', 'Madhya Pradesh', 'Marwadi']
        fifth_ques_s=['All', 'Tamil Nadu', 'Andhra', 'Karnataka', 'Kerala', 'Hyderabadi', 'Mangalorean', 'Chettinad']
        fifth_ques_w=['All','Gujarati', 'Maharashtrian', 'Goan', 'Konkani & Malvani']
        fifth_ques_e=['All','Bengali', 'Odisha', 'Bihari', 'Assam']
        fifth_ques_sf=['All','Mumbai', 'Bengali', 'Maharashtrian', 'Indore']
        options4n=[]
        options4s=[]
        options4w=[]
        options4sf=[]
        options4e=[]
        options4m=[]
        options4f=[]
        
        df5n=pd.DataFrame()
        df5s=pd.DataFrame()
        df5w=pd.DataFrame()
        df5e=pd.DataFrame()
        df5sf=pd.DataFrame()
        df5m=pd.DataFrame()
        df5f=pd.DataFrame()

        # fifth_ques_m=['All']
        # fifth_ques_f=['All','Bengali']
        if('North' in options3):
            options4n=st.sidebar.multiselect('North',fifth_ques_n)
        if('South' in options3):
            options4s=st.sidebar.multiselect('South', fifth_ques_s)
        if('East' in options3):
            options4e=st.sidebar.multiselect('East',fifth_ques_e)
        if('West' in options3):
            options4w=st.sidebar.multiselect('West',fifth_ques_w)
        if('Street Food' in options3):
            options4sf=st.sidebar.multiselect('Street Food',fifth_ques_sf)
        if('Fusion' in options3):
            options4f=['All','Bengali']
        if('Mughlai' in options3):
            options4m=['All']
        
        df5=pd.DataFrame()
        
        # North
        if(len(options4n)!=0):
            if('All' in options4n):
                df5n=df4[df4['Cuisine2'].str.contains('North')]
            else:
                df5n=df4[df4['Cuisine3'].str.contains('|'.join(options4n))]
                # df5=pd.concat([df5,df5n])
        #South
        if(len(options4s)!=0):
            if('All' in options4s):
                df5s=df4[df4['Cuisine2'].str.contains('South')]
            else:
                df5s=df4[df4['Cuisine3'].str.contains('|'.join(options4s))]
                # df5=pd.concat([df5,df5s])
        #East
        if(len(options4e)!=0):
            if('All' in options4e):
                df5e=df4[df4['Cuisine2'].str.contains('East')]
            else:
                df5e=df4[df4['Cuisine3'].str.contains('|'.join(options4e))]
                # df5=pd.concat([df5,df5e])
        #West
        if(len(options4w)!=0):
            if('All' in options4w):
                df5w=df4[df4['Cuisine2'].str.contains('West')]
            else:
                df5w=df4[df4['Cuisine3'].str.contains('|'.join(options4w))]
                # df5=pd.concat([df5,df5w])
        #Street Food
        if(len(options4sf)!=0):
            if('All' in options4sf):
                df5sf=df4[df4['Cuisine2'].str.contains('Street Food')]
            else:
                df5sf=df4[df4['Cuisine3'].str.contains('|'.join(options4sf))]
                # df5=pd.concat([df5,df5sf])
        # #Fusion
        if(len(options4f)!=0):
            df5f=df4[df4['Cuisine2'].str.contains('Fusion')]
            # df5=pd.concat([df5,df5f])
        #Mughlai
        if(len(options4m)!=0):
            df5m=df4[df4['Cuisine2'].str.contains('Mughlai')]
            # df5=pd.concat([df5,df5m])
        df5=pd.concat([df5f,df5m,df5n,df5s,df5e,df5w,df5sf])
        # lastoption=[]
        
        if(len(df5)!=0):
            lastoption=st.multiselect('Ingredients(Type In or Select from Dropdown)',vocabnew)
            
            ing=list(map(str.lower,lastoption))

            includeOptions = st.radio('',('Include Any Ingredient From Above','Include All Ingredients'))

            for i in range(len(ing)):
                ing[i]='|'.join(ing[i].split('/'))
            if(includeOptions == 'Include Any Ingredient From Above'):
                finaldf=df5[df5['Ingredients2'].str.contains('|'.join(ing))]
                # st.write(finaldf[['Dish']].style.hide_index())

                finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
                # finaldf=finaldf.style.format({'nameurl': make_clickable_both})
                for i in range(len(finaldf)):
                    name, url = finaldf.iloc[i]['nameurl'].split('#')
                # return f'<a href="{url}">{name}</a>'
                    # st.markdown(f'<style>.button {{border: none;color: white; padding: 16px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}}.button1 {{background-color: white; color: black; border: 2px solid #602487;}}.button1:hover {{background-color: #602487;color: white;}}</style><a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
                    sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                    st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                if(len(finaldf)==0):
                    st.info('No recipes found')
                    # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
                # optionrecipe=st.selectbox('Recipes',finaldf.Dish.unique())
            else:
                finaldf = showall(ing,df5)
                finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
                for i in range(len(finaldf)):
                    name, url = finaldf.iloc[i]['nameurl'].split('#')
                        # return f'<a href="{url}">{name}</a>'
                            # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

                    sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                    st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                if(len(finaldf)==0):
                    st.info('No recipes found')
        else:
            lastoption=st.multiselect('Ingredients(Type In or Select from Dropdown)',vocabnew)
            
            ing=list(map(str.lower,lastoption))

            includeOptions = st.radio('',('Include Any Ingredient From Above','Include All Ingredients'))

            for i in range(len(ing)):
                ing[i]='|'.join(ing[i].split('/'))
            
            if(includeOptions == 'Include Any Ingredient From Above'):
                finaldf=df4[df4['Ingredients2'].str.contains('|'.join(ing))]
                # st.write(finaldf[['Dish']].style.hide_index())

                finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
                # finaldf=finaldf.style.format({'nameurl': make_clickable_both})
                for i in range(len(finaldf)):
                    name, url = finaldf.iloc[i]['nameurl'].split('#')
                # return f'<a href="{url}">{name}</a>'
                    # st.markdown(f'<style>.button {{border: none;color: white; padding: 16px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}}.button1 {{background-color: white; color: black; border: 2px solid #602487;}}.button1:hover {{background-color: #602487;color: white;}}</style><a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)
                    sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                    st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                if(len(finaldf)==0):
                    st.info('No recipes found')
            else:
                finaldf = showall(ing,df4)
                finaldf['nameurl'] = finaldf['Dish'] + '#' + finaldf['URL']
                for i in range(len(finaldf)):
                    name, url = finaldf.iloc[i]['nameurl'].split('#')
                        # return f'<a href="{url}">{name}</a>'
                            # st.markdown(f'<a href = {url}><button class="button button1">{name}</button></a>',unsafe_allow_html=True)

                    sugg = '<br>'.join(finaldf.iloc[i]['SimLinks'])
                    st.markdown(f'<div class="wrap-collabsible"><input id="collapsible{i}" class="toggle" type="checkbox"><label for="collapsible{i}" class="lbl-toggle">{name}</label><div class="collapsible-content"><div class="content-inner"><a href={url} target="_blank"><button class="button button1">Go To Recipe</button></a><br><p style="font-weight:bold">Other recipes you might like:<p>{sugg}</div></div></div>',unsafe_allow_html=True)
                if(len(finaldf)==0):
                    st.info('No recipes found')


# import streamlit as st
# st.markdown([this is a text link](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png)
# [![this is an image link](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png)](https://streamlit.io)
# # # df3[df3['Cuisine2'].str.contains('|'.join(options3))]


# st.markdown('<footer><h2 style="padding-top:230px">Made by Mahak and Divyam</h2></footer>',unsafe_allow_html=True)
st.sidebar.markdown('<div class="div3"><p style="font-size:14px">Made by <a href="https://www.linkedin.com/in/mahak-agarwal-447494138/" target="_blank">Mahak Agarwal</a>, <a href="https://www.linkedin.com/in/divyam-khanna-a92558118/" target="_blank">Divyam Khanna</a></p><p style="font-size:14px"> Inspired by: <a href="https://www.facebook.com/preety.agarwal.12177" target="_blank">Preety Agarwal</a></p></div>',unsafe_allow_html=True)

