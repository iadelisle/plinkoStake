import streamlit as st
import hashlib
import hmac
from textwrap import wrap
import itertools
import numpy as np





st.title('Plinko')

st.write('''Please enter in your unhashed server seed, your client seed and the nonce you want to check''')

server_seed = st.text_input('Server Seed')
client_seed = st.text_input('Client Seed')
nonceinput = st.text_input('Nonce')

if st.button('Generate Result'):
    #st.write("Button was Pressed")
  #  st.write(server_seed)
   # st.write(client_seed)
   # st.write(nonce)
    workingList = []
    for nonce in range(0, int(nonceinput)):
        message1 = client_seed + ':' + str(nonce) + ":" + "0"
        message2 = client_seed + ":" + str(nonce) + ":" + "1"


        firstOutcomeSet = hmac.new(server_seed.encode(), message1.encode(), hashlib.sha256)

        secondOutcomeSet = hmac.new(server_seed.encode(), message2.encode(), hashlib.sha256)




    # st.write(firstOutcomeSet.hexdigest())
    # st.write(secondOutcomeSet.hexdigest())

    
        val1,  val2, val3, val4 = wrap(firstOutcomeSet.hexdigest()[0:8], 2)

        # st.write(int(val1, 16), int(val2, 16), int(val3, 16), int(val4, 16))

        outcome = ((int(val1, 16) / 256)  + (int(val2, 16) / (256*256)) + (int(val3, 16) / (256*256*256)) + (int(val4, 16) / (256*256*256*256))) * 2

    #   st.write(outcome)

        resultList = [1000, 130, 26, 9, 4, 2, .2, .2, .2, .2, .2, 2, 4, 9, 26, 130, 1000]

        def getPlinkoBase(alphanumeric):
            val1,  val2, val3, val4 = wrap(alphanumeric, 2)
            outcome = ((int(val1, 16) / 256)  + (int(val2, 16) / (256*256)) + (int(val3, 16) / (256*256*256)) + (int(val4, 16) / (256*256*256*256))) * 2
            return int(outcome)

        def getPlinkoSets(initialHexDigest):
            newList = []
            for i in range(0, 8):
                alphanumeric = initialHexDigest[i*8:(i+1)*8]
                outcome = getPlinkoBase(alphanumeric)
                newList.append(outcome)

            return newList
        outcomeList = [firstOutcomeSet, secondOutcomeSet]

        emptyList = []
        for item in outcomeList:
            emptyList.append(getPlinkoSets(item.hexdigest()))

    # st.write(emptyList)
        finalResultList = list(itertools.chain.from_iterable(emptyList))
        
        
       # st.write(sum(finalResultList))
       # st.write(count)
        workingList.append(resultList[sum(finalResultList)])


    #st.write(np.argmax(workingList))
    #st.write(workingList[np.argmax(workingList)])

    st.header(np.mean(workingList))