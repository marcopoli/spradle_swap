# Description
Fork of the original code: https://github.com/allanj/pytorch_neural_crf <br>
Few changes made for using it for the [SpRadIE @ CLEF eHealth competition](https://sites.google.com/view/spradie-2020)

The code has been used for performing NER operations on a dataset of medical records. Many configuration using BERT, RoBERTA, ELECTRA have been evaluated.

All the details are reported in the following [paper](shorturl.at/ahowK).

Please cite:

```python
@inproceedings{polignano2021comparing,
  author    = {Marco Polignano and
               Marco de Gemmis and
               Giovanni Semeraro},
  editor    = {Guglielmo Faggioli and
               Nicola Ferro and
               Alexis Joly and
               Maria Maistro and
               Florina Piroi},
  title     = {Comparing Transformer-based {NER} approaches for analysing textual
               medical diagnoses},
  booktitle = {Proceedings of the Working Notes of {CLEF} 2021 - Conference and Labs
               of the Evaluation Forum, Bucharest, Romania, September 21st - to -
               24th, 2021},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {2936},
  pages     = {818--833},
  publisher = {CEUR-WS.org},
  year      = {2021},
  url       = {http://ceur-ws.org/Vol-2936/paper-68.pdf}
}
```
