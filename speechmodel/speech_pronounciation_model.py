import torch
import torchaudio
import os
import requests
import shutil
import torch.nn as nn
import IPython
from torchaudio.utils import download_asset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import assemblyai as aai
from num2words import num2words
from .scoring_algorithm import ScoringAlgorithm
import subprocess

import nltk
from nltk.corpus import cmudict

class GreedyCTCDecoder(torch.nn.Module):
    def __init__(self, labels, blank=0):
        super().__init__()
        self.labels = labels
        self.blank = blank

    def forward(self, emission: torch.Tensor) -> str:
  
        indices = torch.argmax(emission, dim=-1)  # [num_seq,]
        indices = torch.unique_consecutive(indices, dim=-1)
        indices = [i for i in indices if i != self.blank]
        return "".join([self.labels[i] for i in indices])
    
class SpeechToText:

    def __init__(self, file):
        self.file = file

    def model_evaluate(self):

        aai.settings.api_key = "8461624cc9884f1484e5b565ef1657f8"
        
        transcriber = aai.Transcriber()
        SPEECH_FILE = self.file
       #current_directory = os.getcwd()
    
    # Define the path to save the file
        #save_path = os.path.join(current_directory, self.file)
    
        #SPEECH_URL = os.path.join(os.path.dirname(__file__), "finnish.mp3")
        SPEECH_URL = "recording.mp3"
    
        # current_directory = os.getcwd()
    
        # # Define the path to save the file
        # save_path = os.path.join(current_directory, SPEECH_FILE)
        
        # # Open the destination file in write-binary mode and save the content
        # with open(save_path, 'wb') as f:
        #     # Write the file content
        #     f.write(self.file.read())
        # output_path = os.path.join(current_directory, 'saved_file.mp3')

        # subprocess.run(
        #     ['ffmpeg', '-i', save_path, output_path],
        #     check=True,
        #     stdout=subprocess.PIPE,
        #     stderr=subprocess.PIPE
        # )
        # with open(output_path, 'rb') as mp3_file:
        # # Read and process the MP3 file content (you can also return it or do other operations)
        #     SPEECH_URL = mp3_file.read()
        # print(f"File saved to {save_path}")

        # current_directory = os.path.dirname(os.path.abspath(__file__))

        # # # List all files in the current directory
        # files_in_directory = os.listdir(current_directory)

        # # Print out all files
        # for file in files_in_directory:
        #     if file == "dialectaccent_vol_01_01jvw.mp3":
        #         SPEECH_URL = file
        #         print("hello")
        # os.makedirs(os.path.dirname(SPEECH_FILE), exist_ok=True)
        # self.file.save(SPEECH_FILE)
        # SPEECH_URL = "dialectaccent_vol_01_01jvw.mp3"
      

        # Convert file to MP3 format
        # output_mp3 = os.path.splitext(SPEECH_FILE)[0] + '.mp3'
        # subprocess.run(['ffmpeg', '-i', SPEECH_FILE, '-vn', '-ar', '44100', '-ac', '2', '-b:a', '192k', output_mp3], check=True)

        transcriber = aai.Transcriber()
        transcript_trained = transcriber.transcribe(SPEECH_URL)
        


        torch.random.manual_seed(0)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # #SPEECH_FILE = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav")
        bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H

        model = bundle.get_model().to(device)

        waveform, sample_rate = torchaudio.load(SPEECH_FILE)
        waveform = waveform.to(device)
        if sample_rate != bundle.sample_rate:
            waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)

        with torch.inference_mode():
            features, _ = model.extract_features(waveform)

        # fig, ax = plt.subplots(len(features), 1, figsize=(16, 4.3 * len(features)))
        # for i, feats in enumerate(features):
        #     ax[i].imshow(feats[0].cpu(), interpolation="nearest")
        #     ax[i].set_title(f"Feature from transformer layer {i+1}")
        #     ax[i].set_xlabel("Feature dimension")
        #     ax[i].set_ylabel("Frame (time-axis)")
        # fig.tight_layout()

        with torch.inference_mode():
            emission, _ = model(waveform)

      
        decoder = GreedyCTCDecoder(labels=bundle.get_labels())
        transcript_untrained = decoder(emission[0])
        error_indicies = [1, 2, 3, 6, 7]
        sentences = ["Hello", "this", "is", "how", "to", "build", "an", "application", ",", "thank", "you"]
        #return sentences, error_indicies
        return self.data_processing(transcript_trained, transcript_untrained)

    def data_processing(self, transcript_trained, transcript_untrained): 
        d = cmudict.dict()
        number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        words_trained = []
        words_untrained = []
        word_trained = ""
        word_untrained = ""
        print("hello")
        for i in transcript_untrained:
            if i == "|":
                words_untrained.append(word_untrained.lower())
                word_untrained = ""
            else:
                word_untrained+=i

        for i in transcript_trained.text:
            
            if i == " ":
                words_trained.append(word_trained.lower())
                word_trained = ""
            elif i != ",":
                
                add = True
                for x in number_list:
                    if x in i:
                        words_trained.append(num2words(int(i)))
                        add = False
                        break
                if add:
                    word_trained+=i
        words_trained = [item for item in words_trained if item != ""]
        words_untrained = [item for item in words_untrained if item != ""]

        phenomes_trained = []
        phenomes_untrained = []

        for word in words_trained:
            if word in d:           
                phenomes_trained.append(d[word])          
        
        for word in words_untrained:
            if word in d:          
                phenomes_untrained.append(d[word])
                
        python_scorer = ScoringAlgorithm(phenomes_trained, phenomes_untrained)
        scores = python_scorer.scoring_algorithm()
        indicies = []
        for i in range(len(scores)):
       
            if scores[i] > 0.89:
                indicies.append(i)
        # print(words_trained)
        # print(indicies)
        return words_trained, indicies 
       
