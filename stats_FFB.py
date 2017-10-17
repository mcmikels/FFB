#Calcuate stats for FFB

import numpy
import FFB

#Calcuate mean and sigma for each team

RIW_mean = numpy.mean(FFB.righteous_in_wrath_scores)
RIW_sigma = numpy.std(FFB.righteous_in_wrath_scores)

TSW_mean = numpy.mean(FFB.toms_shady_weinerz_scores)
TSW_sigma = numpy.std(FFB.toms_shady_weinerz_scores)

four_mean = numpy.mean(FFB.fournettecate_scores)
four_sigma = numpy.std(FFB.fournettecate_scores)

BOT_mean = numpy.mean(FFB.big_ol_TDs_scores)
BOT_sigma = numpy.std(FFB.big_ol_TDs_scores)

EM_mean = numpy.mean(FFB.equipmunk_managers_scores)
EM_sigma = numpy.std(FFB.equipmunk_managers_scores)

FHQ_mean = numpy.mean(FFB.fhqwhgads_scores)
FHQ_sigma = numpy.std(FFB.fhqwhgads_scores)

butts_mean = numpy.mean(FFB.butts_scores)
butts_sigma = numpy.std(FFB.butts_scores)

LMQ_mean = numpy.mean(FFB.lick_my_quintorris_scores)
LMQ_sigma = numpy.std(FFB.lick_my_quintorris_scores)

MK_mean = numpy.mean(FFB.menstrual_krampus_scores)
MK_sigma = numpy.std(FFB.menstrual_krampus_scores)

SITA_mean = numpy.mean(FFB.stranger_in_the_alps_scores)
SITA_sigma = numpy.std(FFB.stranger_in_the_alps_scores)

MOD_mean = numpy.mean(FFB.mother_of_dragons_scores)
MOD_sigma = numpy.std(FFB.mother_of_dragons_scores)

WAC_mean = numpy.mean(FFB.wit_and_creativity_scores)
WAC_sigma = numpy.std(FFB.wit_and_creativity_scores)

all_means = [RIW_mean,TSW_mean,four_mean,BOT_mean,EM_mean,FHQ_mean,butts_mean,
LMQ_mean,MK_mean,SITA_mean,MOD_mean,WAC_mean]

all_sigma = [RIW_sigma,TSW_sigma,four_sigma,BOT_sigma,EM_sigma,FHQ_sigma,butts_sigma,
LMQ_sigma,MK_sigma,SITA_sigma,MOD_sigma,WAC_sigma]

mean_dictionary = dict(zip(FFB.teams,all_means))
sigma_dictionary = dict(zip(FFB.teams,all_sigma))

print "Stats done"
