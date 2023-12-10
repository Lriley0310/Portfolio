# We need to import core packages.
# streamlit is an open source Python UI
import requests
import streamlit as st
import streamlit.components.v1 as stc

# Import EDA packages.
import pandas as pd

# Neattext is used for regular expression parts of the program, this incluses extract_emails, extract_urls, extract_phone_numbers
import neattext.functions as nfx

# Import Utils.
#
import base64

# Used to help create a timestamp for our files.
import time

# Function to get the time stamp. 
# Y = year,
# m = month,
# d = day,
# H = hour, 
# M = minute, 
# S = second.
timestr = time.strftime("%Y%m%d-%H%M%S")

# Fxn to Download
# This will convert our data into a csv file.
# This one is specific to task type. Refer to the line new_filename. 
# For example, this is used in the single extractor where the user picks 
# the data type they wish to extract.
def make_downloadable(data,task_type):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()  # B64 encoding
    st.markdown("### ** Download Results File ** ")
    new_filename = "extracted_{}_result_{}.csv".format(task_type,timestr)
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Fxn to Download
def make_downloadable_df(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()  # B64 encoding
    st.markdown("### ** Download CSV File ** ")
    new_filename = "extracted_data_result_{}.csv".format(timestr)
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Let's make our function for URL compatibility.
@st.cache_data
def fetch_query(query):
    base_url = "https://www.google.com/search?q={}".format(query)
    r = requests.get(base_url)
    return r.text

def main():
    """Email Extraction Application"""

    # Create a menu for the application.
    menu = ["Home", "Single Extractor", "Bulk Extractor", "About"]

    # Create choice for the user
    choice = st.selectbox("Menu", menu)

    if choice == "Home":

        #Using streamlit here, not sure if we will actually want to use streamlit in our web app. I need to talk to the team and ask them about it.
        st.subheader("Search and Scrape")

        # List of countries 
        countries_list = ["USA", "Afghanistan","Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Austrian Empire", "Azerbaijan", "Baden*", "Bahamas, The", "Bahrain", "Bangladesh", "Barbados", "Bavaria*", "Belarus", "Belgium", "Belize", "Benin (Dahomey)", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Brunswick and Lüneburg", "Bulgaria", "Burkina Faso (Upper Volta)", "Burma", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands, The", "Central African Republic", "Central American Federation*", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo Free State, The", "Costa Rica", "Cote d’Ivoire (Ivory Coast)", "Croatia", "Cuba", "Cyprus", "Czechia", "Czechoslovakia", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Duchy of Parma, The*", "East Germany (German Democratic Republic)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Federal Government of Germany (1848-49)*", "Fiji", "Finland", "France", "Gabon", "Gambia, The", "Georgia", "Germany", "Ghana", "Grand Duchy of Tuscany, The*", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Hanover*", "Hanseatic Republics*", "Hawaii*", "Hesse*", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kingdom of Serbia/Yugoslavia*", "Kiribati", "Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Lew Chew (Loochoo)*", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mecklenburg-Schwerin*", "Mecklenburg-Strelitz*", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nassau*", "Nauru", "Nepal", "Netherlands, The", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North German Confederation*", "North German Union*", "North Macedonia", "Norway", "Oldenburg*", "Oman", "Orange Free State*", "Pakistan", "Palau", "Panama", "Papal States*", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Piedmont-Sardinia*", "Poland", "Portugal", "Qatar", "Republic of Genoa*", "Republic of Korea (South Korea)", "Republic of the Congo", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Schaumburg-Lippe*", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands, The", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Texas*", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Two Sicilies*", "Uganda", "Ukraine", "Union of Soviet Socialist Republics*", "United Arab Emirates, The", "United Kingdom, The", "Uruguay", "Uzbekistan", "USA","UK", "Vanuatu", "Venezuela", "Vietnam", "Württemberg*", "Yemen", "Zambia", "Zimbabwe"]

        # List of email extensions.
        email_extensions_list = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr", "gmx.de", "web.de", "yandex.ru", "ymail.com", "libero.it", "outlook.com", "uol.com.br", "bol.com.br", "mail.ru", "cox.net", "hotmail.it", "sbcglobal.net", "sfr.fr", "live.fr", "verizon.net", "live.co.uk", "googlemail.com", "yahoo.es", "ig.com.br", "live.nl", "bigpond.com", "terra.com.br", "yahoo.it", "neuf.fr", "yahoo.de", "alice.it", "rocketmail.com", "att.net", "laposte.net", "facebook.com", "bellsouth.net", "yahoo.in", "hotmail.es", "charter.net", "yahoo.ca", "yahoo.com.au", "rambler.ru", "hotmail.de", "tiscali.it", "shaw.ca", "yahoo.co.jp", "sky.com", "earthlink.net", "optonline.net", "freenet.de", "t-online.de", "aliceadsl.fr", "virgilio.it", "home.nl", "qq.com", "telenet.be", "me.com", "yahoo.com.ar", "tiscali.co.uk", "yahoo.com.mx", "voila.fr", "gmx.net", "mail.com", "planet.nl", "tin.it", "live.it", "ntlworld.com", "arcor.de", "yahoo.co.id", "frontiernet.net", "hetnet.nl", "live.com.au", "yahoo.com.sg", "zonnet.nl", "club-internet.fr", "juno.com", "optusnet.com.au", "blueyonder.co.uk", "bluewin.ch", "skynet.be", "sympatico.ca", "windstream.net", "mac.com", "centurytel.net", "chello.nl", "live.ca", "aim.com", "bigpond.net.au"] 

        # Drop down box for country selection.
        country_name = st.selectbox("Country", countries_list)

        # Drop down for email extension selection.
        email_type = st.selectbox("Email Type", email_extensions_list)

        # Drop down for user to select what they want to extract. 
        task_list = ["Emails", "URLS", "Phonenumbers"]
        task_option = st.multiselect("Task", task_list, default="Emails")

        # User needs to enter the search term or job they are looking for. 
        # The option Jake initially shared was "Dentist",
        # dentist would be a valid input here.
        search_text = st.text_input("Paste Term Here")

        # Creating our query format.
        # "gmail.com" and "dentist" site:linkedin.com (+ country)
        generated_query = f"email@{email_type} + {search_text} + linkedin.com"
        st.info("Generated Query: {}".format (generated_query))

        # Now we need to fetch the query we generated above.
        if st.button("Search & Extrract"):
            if generated_query is not None:
                text = fetch_query(generated_query)

                # Comment out the bulk data, this is the raw data extracted, simlilar to what is in practice.txt. 
                # We don't want the users to have to look at this.
                # st.write(text)

                # Same code herre as the bulk extractor.
                task_mapper = {"Emails":nfx.extract_emails(text), "URLS":nfx.extract_urls(text), "Phonenumbers":nfx.extract_phone_numbers(text)}
                all_results = []
                for task in task_option:
                    result = task_mapper[task]

                    # Comment out the initial result write, or else we end up with results that will 
                    # be redundant to the user, but it is important for the program.
                    # st.write(result)

                    # Now lets append it into a dataframe.
                    # First we put the list into another list.
                    all_results.append(result)
                st.write(all_results)
        
                # Now lets add it into a dictionary.
                with st.expander("Results As DataFrame"):

                     # The T here is very important. This gives us the table view that we want to see.
                    result_df = pd.DataFrame(all_results).T
                    result_df.columns = task_option
                    st.dataframe(result_df)
            
                    # Now lets use the dataframe made above for the bulk extractor.
                    # This allows us to get a CSV of this data.
                    make_downloadable_df(result_df)

    # Single extractor is used for when a user only wants to extract one datatype.
    elif choice == "Single Extractor":
        st.subheader("Extract a Single Term")
        text = st.text_area("Paste Text Here")
        task_option = st.selectbox("Task", ["Emails", "URLS", "Phonenumbers"])

        # This option is for when we manually copy and paste the search reults from google. 
        # There is already a saved search in practice.txt for us to use.
        # The specific search data came from the search "dentist + USA + email@gmail.com"
        # Look at how this is working, 
        # Neattext allows for us to simply extract this information with the built in functions in its libraries.
        # Email = extract_emails
        # PhoneNumber = extract_phone_number
        # URLS = extract_urls
        # Because this is a text based extraction, we will use the variable text 
        # so that it knows we are using a string.
        if st.button("Extract"):
            
            # It is specifically ordered this way, so that if there is nothing to return for either the URL or
            # phone number, because phone numbers and URLS are not always included, 
            # You will always get at least the emails returned. You can play around with it if
            # you would like a better understanding of what I mean.
            if task_option == "URLS":
                results = nfx.extract_urls(text)
            elif task_option == "Phonenumbers":
                results = nfx.extract_phone_numbers(text)
            else:
                results = nfx.extract_emails(text)
            st.write(results)
            
            # This part is underneath the extraction results.
            # There will be a button that says "Results as Dataframe", 
            # That is what I named the expander. 
            # The expander when clicked, will display the results as a dataframe. 
            # This is using the pandas module to format the results
            # and streamlit to display the results.
            with st.expander("Results As DataFrame"):
                result_df = pd.DataFrame({'Results:':results})
                st.dataframe(result_df)

                # Now let's convert the data into a csv file.
                # If you click on the data_frame results, a new button will pop up that says 
                # "Click Here", if you click it, it will download a csv file with the extracted data.
                make_downloadable(result_df, task_option)




    # This is for the bulk extractor.
    # Notice how for the bulk extractor we can select multiple options 
    # of what we want extracted. We can select up to all 3.
    # We will have it default to emails, as that was the original intention for
    # our website.
    # This time, we have the options automatically return as the user selects them, no need for double selection.
    elif choice == "Bulk Extractor":
        st.subheader("Bule Extractor")
        text = st.text_area("Paste Text Here")
        task_list = ["Emails", "URLS", "Phonenumbers"]
        task_option = st.multiselect("Task", task_list, default="Emails")
        task_mapper = {"Emails":nfx.extract_emails(text), "URLS":nfx.extract_urls(text), "Phonenumbers":nfx.extract_phone_numbers(text)}
        all_results = []
        for task in task_option:
            result = task_mapper[task]

            # Comment out the initial result write, or else we end up with results that will 
            # be redundant to the user, but it is important for the program.
            # st.write(result)

            # Now lets append it into a dataframe.
            # First we put the list into another list.
            all_results.append(result)
        st.write(all_results)
        
        # Now lets add it into a dictionary.
        with st.expander("Results As DataFrame"):

            # The T here is very important. This gives us the table view that we want to see.
            result_df = pd.DataFrame(all_results).T
            result_df.columns = task_option
            st.dataframe(result_df)
            
            # Now lets use the dataframe made above for the bulk extractor.
            # This allows us to get a CSV of this data.
            make_downloadable_df(result_df)

    else: 
        st.subheader("About")

if __name__ == '__main__':
    main()