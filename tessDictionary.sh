#unpack everything (i did this just to back up my eng.word-dawg, you'll also need the unicharset later)

    ./combine_tessdata -u eng.traineddata

#    create a textfile of your wordlist (wordlistfile)

#    create a eng.word-dawg

    ./wordlist2dawg wordlistfile eng.word-dawg traineddat_backup/.unicharset

#    replace the word-dawg file

    ./combine_tessdata -o eng.traineddata eng.word-dawg

