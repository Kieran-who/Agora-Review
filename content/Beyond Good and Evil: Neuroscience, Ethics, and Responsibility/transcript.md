---
title: 'Beyond Good and Evil? Neuroscience, Ethics, and Responsibility - Transcript'
date: '2025-09-12'
prev:
  text: See write up
  link: '/Beyond Good and Evil: Neuroscience, Ethics, and Responsibility/summary.md'
next: false
---

### Speaker: Host

Dr. Mercado, the authors claim that even if we discover robust brain–behavior laws, ethical categories like “intention” and “evil” cannot be eliminated because their application-criteria live in social practices, and they allege a circularity: we must first use moral concepts to pick which behaviors count as “evil” before we can model their neural bases. Within your neurofunctional normativity program, could you specify—concretely—(a) an operational test that would license replacing “intention to kill” with a neural descriptor in a Jones-style homicide case, and (b) the falsification conditions that would show your replacement fails? In particular, how do you avoid smuggling normative judgments into the definition of the circuit pattern you would label as “evil”?

---

### Speaker: Dr. Iris K. Mercado

Thank you. Let me be maximally concrete.

First, I would not try to replace “intention to kill” with a single blob of activation. The right unit is a computational state: a goal‑directed policy that assigns positive expected value to another agent’s death and drives plan construction to achieve it. Call this the lethal‑goal policy state (LGPS). It is a latent variable we can estimate jointly from behavior and neural data.

(a) An operational test for replacement in a Jones‑style case

Define LGPS without moral vocabulary, using only observables and computational constructs:

- Task family: Naturalistic decision tasks (VR and tabletop) with branching opportunities where a participant can choose among options that differ along orthogonal dimensions: (i) incapacitate/kill a target agent, (ii) neutralize and flee, (iii) acquire resources, (iv) do nothing. The outcomes are biophysical and behavioral (e.g., in VR, “target’s physiology goes to zero,” or “agent disables the target and exits”), not moral labels. In separate variants we dissociate instrumental aggression from reactive/impulsive harm and from accidents.

- Behavioral model: Fit inverse reinforcement learning (IRL) to action sequences to recover a reward function R(s,a) with weights on outcome features, including a “target death” feature. LGPS is present when the inferred weight on target death is positive and dominates alternatives after controlling for threat, self‑preservation, and resource acquisition.

- Neural descriptor: Train a preregistered composite biomarker N‑KILL to estimate LGPS from neural data. Features are theory‑driven and task‑independent:
  1. Value code: vmPFC/ventral striatum Q‑value patterns assigning high value to state trajectories terminating in target death, dissociable from mere arousal.
  2. Prospection: hippocampal–prefrontal forward replay sequences that preferentially simulate lethal plans; replay content decoded to target identity and terminal state.
  3. Control/inhibition profile: effective connectivity showing top‑down dLPFC→amygdala/striatum drive with concomitant down‑weighting of rIFG/stop‑network responses to victim‑harm representations.
  4. Other‑regard suppression: blunted TPJ/medial PFC responses to simulated victim outcomes, specifically during plan evaluation (not globally).
  5. Policy stability: persistence and generalization of the above across superficially different contexts that afford the same lethal end.

Operational test battery and success criteria:

- Predictive sufficiency: In held‑out contexts, N‑KILL estimated 5–30 seconds prior to action predicts selection of lethal options with AUC ≥ 0.90 and PPV calibrated to base rates; time‑generalization across tasks.

- Causal manipulability: Closed‑loop perturbation (e.g., rTMS/DBS or targeted pharmacology) that selectively disrupts the dLPFC–vmPFC–amygdala network when N‑KILL is high reduces the probability of lethal action by ≥50% without degrading basic motor execution, general threat detection, or non‑lethal self‑preservation choices.

- Representational specificity: MVPA decodes lethal goal content (who is to be harmed; terminal state) from vmPFC/hippocampal patterns above stringent permutation baselines; representational similarity matches the IRL‑derived plan tree.

- Reasons‑responsiveness equivalence: When strong countervailing reasons are supplied (credible new information about consequences, norms, incentives), the same network shows systematic, model‑predictable value updating and replay redirection. If the neural state tracks reasons the way “intention” is supposed to, functional equivalence is established.

- Cross‑species and lesion convergence: Homologous features predict instrumental conspecific aggression in animal models; focal lesions along the same circuit produce double dissociations (loss of instrumental lethal planning with spared reactive aggression, or vice versa).

If a Jones‑like defendant had high‑fidelity pre‑act neural data showing LGPS by these criteria, and if perturbing the detected state reliably altered lethal choice disposition in controlled probes, we would have grounds to replace “intention to kill” with the neural/computational descriptor for forensic purposes.

(b) Falsification conditions

The replacement fails—full stop—if any of the following obtain:

- Predictive failure: N‑KILL does not predict lethal action above robust situational baselines, or collapses outside of its training contexts.

- Causal failure: Targeted disruption of the putative circuit does not change lethal action probability, or only changes it by globally degrading motor function/arousal (no selective effect on lethal planning).

- Specificity failure: The signature appears in accidents, in non‑lethal competitive planning, or in mere high arousal; or it systematically misses clear cases of deliberate lethal planning (double dissociations in both directions).

- Representation failure: We cannot decode lethal plan content or value assignments beyond chance; replay does not differentiate lethal vs non‑lethal trajectories in the predicted way.

- Reasons‑neural mismatch: Manipulations that alter reasoned choice (credible new information or normative constraints) change behavior while the neural descriptor does not budge, or the network changes while behavior remains reasons‑responsive in the opposite direction.

- Non‑natural‑kind failure: Unsupervised latent‑state discovery across labs, tasks, and species does not recover a stable cluster corresponding to LGPS; the best model of behavior is social/situational with neural features adding no explanatory/predictive power.

Avoiding normative smuggling

Three safeguards:

- Outcome and computation, not moral labels: We define the target variable via physical outcomes (e.g., termination of a conspecific agent in the task world) and the computational property “positive valuation of another’s death driving plan construction,” inferred from IRL. No “evil,” “malice,” or legal categories are used in model training.

- Unsupervised discovery and preregistration: Use unsupervised/hierarchical Bayesian models to discover latent states that best explain action selection across tasks. Only after the fact do we ask which latent state aligns with lethal goal pursuit. Feature sets, thresholds, and causal tests are preregistered to prevent post hoc rebranding.

- Cross‑context generalization and double‑dissociation: Demonstrate that the same neural state recurs across ethically neutral contexts (e.g., predator‑prey analogs, competitive games) whenever the computational criterion holds, and that nearby states (reactive rage, careless risk‑taking) dissociate. That guards against baking our local moral grammar into the descriptor.

Two clarifications in light of the Wittgenstein/Chomsky concerns raised by Prof. Steinbruck and Dr. Rahman:

- I am not claiming current science meets this bar; I am specifying the bar. If we can reach predictive, causal, representational, and generalization sufficiency, then for many legal purposes “intention to kill” becomes an unnecessary theoretical posit—a place‑holder for an LGPS‑type state. If we cannot, we should not displace the folk term.

- Normativity reenters at the policy layer. Choosing to care about “death of a conspecific” as a salient outcome is indeed tied to our form of life. The descriptor itself is value‑neutral; what we do with it (culpability, sentencing) is a separate, explicitly normative decision. I am happy to keep that division of labor visible.

In the interim, I would use N‑KILL‑like measures to inform risk and treatment in a reasons‑responsiveness framework (with Justice Okafor’s constraints), not to replace legal concepts. Only when the operational tests above are passed—and the falsifiers fail—would I endorse replacement.

---

### Speaker: Host

Prof. Steinbruck, take Dr. Mercado’s proposed LGPS/N‑KILL bar at face value: suppose it achieves predictive, causal, and representational sufficiency and tracks reasons updates. Consider three concrete contexts with matched neural/computational signatures: (1) a contract assassin selecting a lethal plan; (2) a combatant lawfully engaging an enemy under rules of engagement; (3) a palliative‑care physician administering analgesia foreseeing but not desiring death (double‑effect). If the same LGPS‑type state is detected and manipulable across all three, does that license replacing “intention to kill” with the neural descriptor, or is there a grammar of intention—tied to avowals, justificatory uptake, and role‑governed permissions—that cannot be captured even under Mercado’s success conditions? Please identify one decisive practice‑based asymmetry that would remain, and explain why it is conceptually irreducible (or, if you think it is bridgeable, specify what additional evidence would be required).

---

### Speaker: Prof. Leda Steinbruck

Thank you. I’ll grant Dr. Mercado her strongest case: suppose LGPS/N‑KILL really does everything she asks of it—predicts, is causally manipulable, decodes plan content, and tracks informational updates—across the assassin, the ROE‑compliant combatant, and the palliative‑care physician.

One decisive practice-based asymmetry would still remain: the means/side‑effect criterion as it functions in our practices of giving and asking for reasons, tested by counterfactual commitment and avowal within role‑governed institutions.

- How it works in our grammar: When we ask “Did she intend to kill?”, we don’t just look for an inner policy. We ask whether the death figures as her end or as a means in her practical reasoning, as opposed to a foreseen but undesired side‑effect. We test this by a counterfactual: if death would not occur, would she still do what she did? We also take seriously what the agent can sincerely avow as her reason, and whether that avowal is intelligible and taken up as justificatory within the relevant practice (medicine, war, criminal law).

- Applied to your three cases:
  1. Contract assassin: death of the target is part of the end/means structure. If the target could not be killed, the plan collapses. Avowals to that effect (“I was hired to kill”) fit the practice and license blame.
  2. Lawful combatant: often, yes, death of the enemy is intended as a means to a permitted military objective. The same bodily movement is not “murder” because the role‑governed permissions of the practice transform its normative status; the avowal “I aimed to neutralize/kill under ROE” is taken up as a justification, not an inculpation.
  3. Palliative physician: the intention is relief of suffering; death is foreseen and tolerated, not aimed at. The counterfactual test bites: if the same analgesia could be given without shortening life, she would choose that. Her avowal (“I intended analgesia, not death”) has default authority in the medical practice and, when congruent with dosing, protocols, etc., is exculpatory.

Why this is conceptually irreducible: On a Wittgenstein–Anscombe view, these are not empirical afterthoughts added to a neural core; they are part of the criteria for the correct application of “intends” in our language‑games. The concept’s point is to locate an act within a nexus of reasons, permissions, and responsibilities. That nexus is constituted by public rules of medicine, war, and law—by what counts as a reason for what—rather than by any inner state alone. Even a perfect neural correlate of “positively valuing terminal states for a conspecific and constructing plans toward them” underdetermines whether, in our practices, we should say “she intended to kill” or “she intended to palliate, foreseeing death,” because what follows from the ascription (blame, justification, immunity) is fixed by those practices.

Notice the dilemma your stipulation creates. Either:

- LGPS is truly the same across the three cases, in which case it fails to track the very means/side‑effect distinction that partly constitutes our concept of intention; or
- LGPS is refined so that it does not light up in the palliative case (because death is not positively weighted), in which case the “same signature” premise drops out and the neural descriptor has simply been tuned to our existing normative criterion.

Could this gap be bridged? Only by building the practice back in—by enriching the “descriptor” with the agent’s avowals, counterfactual commitments, and role‑permissions, and by treating uptake within the relevant institution as constitutive evidence. But then the replacement collapses into a hybrid: a neural‑plus‑normative status that inherits its authority from the practice you hoped to supplant.

So my answer is no: even on Dr. Mercado’s most successful day, a neural/computational state cannot replace “intention to kill.” It can be excellent evidence about capacities, risk, and the causal organization of planning; it cannot bear the justificatory and role‑indexed load that our intention‑ascriptions carry. That load is not an add‑on at the “policy layer”; it is the grammar of the concept.

---

### Speaker: Host

Dr. Rahman, can the means/side‑effect asymmetry that Prof. Steinbruck insists is constitutive of our intention concept be captured at the computational level without smuggling in normative practice—e.g., by representing hierarchical plans where an outcome features as a causal subgoal (means) vs a probabilistic collateral outcome (side‑effect), tested by counterfactual invariance (would the agent still select the same plan in worlds where the collateral outcome is suppressed)? If so, specify the computational signature and an implementational prediction that would distinguish the assassin from the palliative‑care physician under Dr. Mercado’s LGPS framework. If not, explain why this is a levels mistake: what remains explanatorily and normatively un‑reducible even if such counterfactual‑sensitive planning states were neurally identified? And in either case, should such a model license replacement of “intention to kill,” or only provide high‑grade evidence within a reasons‑responsiveness account of culpability?

---

### Speaker: Dr. Samuel N. Rahman

Short answer: you can capture a large part of the means/side‑effect asymmetry at the computational level, but even a successful neural instantiation would not license replacing “intention to kill.” It would give very probative evidence about the agent’s planning architecture and reasons‑responsiveness; the justificatory and role‑indexed content that our intention ascriptions carry remains at the level of practice.

What a computational signature would look like

Think hierarchical planning plus counterfactual sensitivity. In a hierarchical RL/IRL framework:

- Goal structure

  - Assassin: the victim’s death (D) is a required instrumental subgoal on all optimal trajectories to the agent’s higher‑level goal G. Formally, D is a necessary node in the plan graph; removing D collapses plan optimality.
  - Palliative physician: analgesia/relief (A) is the terminal goal; D is an anticipated collateral outcome with non‑positive weight. D is not a required node for achieving A.

- Reward gradients

  - Assassin: ∂U/∂D > 0 (death carries positive marginal utility, all else equal).
  - Physician: ∂U/∂D ≤ 0 (death carries zero or negative marginal utility; A carries the positive weight).

- Counterfactual invariance test
  - Intervene on the model to set P(D)=0 while holding feasibility of A or G fixed.
    - Assassin: policy switches (or becomes undefined). If death is made unattainable but other conditions remain, the agent either abandons the plan or searches for an alternative path that reinstates D.
    - Physician: policy is invariant. If the same analgesia can be achieved with no death, that plan is preferred.

Implementational predictions under an LGPS‑style framework

If you implement the above computational differences, you should see dissociable neural signatures:

- Sign of value and prediction errors

  - vmPFC/ventral striatum encodes higher state‑action values for trajectories culminating in D for the assassin; equal or lower values for the physician. Dopamine‑like RPEs at the moment of D are positive for the assassin, neutral/negative for the physician when A is held constant.

- Replay content and necessity

  - Hippocampal–PFC forward replay prioritizes D‑containing sequences for the assassin and treats D as a bottleneck; in the physician, replay prioritizes A‑achieving sequences and prunes D when a non‑lethal route is available.

- Counterfactual manipulation

  - In VR tasks where an “analgesia‑without‑death” option is introduced, the assassin’s lethal‑plan network (dLPFC–vmPFC–hippocampus) drops out or reorganizes; the physician’s planning network remains engaged on the same task with unchanged high‑level policy.

- Harm‑valuation and control

  - Assassin: positive coupling between dLPFC and striatum when evaluating D as a means; attenuated rIFG/stop‑network responses to simulated harm. Physician: intact or heightened harm‑sensitivity (TPJ/insula) co‑occurring with pursuit of A, and rIFG engagement when avoidable harm appears.

- Causal perturbation asymmetry
  - Closed‑loop down‑weighting of the “death value” channel (e.g., temporally precise disruption of vmPFC coding of D as a subgoal) reduces lethal plan selection for the assassin but leaves the physician’s choice of A unaffected; enhancing availability of non‑lethal A‑paths has little effect on the assassin if D retains positive weight, but immediately flips the physician’s policy.

What if LGPS/N‑KILL “looks the same” in assassin and palliative care?

Then the descriptor is too coarse. A model that simply flags “positive expected value on terminal states for a conspecific” will, by construction, miss the means/side‑effect contrast. The fix is exactly the counterfactual/graph‑structural ingredients above: require evidence that D is a required subgoal with positive marginal utility and plan‑level necessity. If you add those, the palliative case should fall out of LGPS.

Why replacement still overreaches

- Levels mistake. The means/side‑effect difference you can encode computationally is a difference in plan architecture and value assignment. Our concept “intends to kill” does more: it locates the act within a nexus of avowals, role‑governed permissions, and justificatory uptake. Whether the same bodily movement is murder, lawful combat, or double‑effect palliative care turns on institutional norms and what counts as a reason within those practices. That is not an implementational fact to be read off a circuit; it’s constitutive of the concept’s use.

- Explanatory gap caution. Even if you map the computational signatures to multi‑area neural dynamics with impressive predictive/causal success, identity claims (“intention just is LGPS/N‑KILL”) are premature. Multiple implementational realizations can underwrite the same computational property; and the move from a state’s causal role to its justificatory status is not a move neuroscience can, or should, make.

- Normativity does not evaporate. Choosing which outcome features matter (e.g., “death of a conspecific”) already reflects our form of life. More importantly, the downstream consequences of saying “he intended to kill”—blame, excuse, permission—are settled by legal/ethical rules, not by the presence of a neural state.

So, how should such a model be used?

- As high‑grade evidence within a reasons‑responsiveness framework of culpability. It can speak to capacity (could the agent grasp and respond to reasons?), to the organization of planning (was death a necessary means vs tolerated side‑effect?), and to the likely efficacy of interventions.

- Not as a replacement for the intention concept in law or ethics. Keep the space of reasons intact. Let neural/computational evidence update our posterior over the latent “intention” variable together with avowals, situational facts, and role‑constraints, but do not collapse the normative category into a circuit label.

In short: yes to a computational capture of the core structural contrast, yes to implementational predictions that ought to separate assassin from physician, and no to conceptual replacement. The right division of labor is computational models for explanatory and predictive leverage; normative practices for justification and desert.

---

### Speaker: Host

Justice Okafor, assume Dr. Mercado’s N‑KILL/LGPS package meets her stringent bar: it predicts lethal plan selection, is causally manipulable, decodes plan content, and tracks countervailing reasons across assassin, combatant under ROE, and palliative‑care contexts. In a homicide trial, would you admit such evidence to prove the mens rea element (intent to kill), or would you confine it to capacity/risk/sentencing? Please be operational: (1) set out admissibility criteria (Daubert/Rule 702‑style factors and a relevance fit test) tailored to this kind of neural evidence; (2) specify the precise legal questions it may inform and those it must not supplant under a reasons‑responsiveness model; and (3) draft a limiting instruction you would give to jurors to prevent equating the neural signature with culpability or collapsing the means/side‑effect distinction (e.g., physician double‑effect). If you think there is any context where N‑KILL should be excluded despite technical validity (e.g., palliative care), identify that boundary and why.

---

### Speaker: Hon. Naomi Okafor, JD, DPhil

Thank you. Even on Dr. Mercado’s best‑case assumptions, I would not let N‑KILL/LGPS stand in for mens rea. I would treat it as high‑grade, but bounded, evidence about planning architecture and reasons‑responsiveness. In the guilt phase, it can corroborate or undercut claims about purpose/knowledge; it cannot decide intention, collapse the means/side‑effect distinction, or displace justificatory defenses. In most cases I would confine it to capacity and sentencing; in a narrow class (e.g., the “contract‑assassin” fact pattern with temporally locked pre‑act data), I would allow it as corroborative of purpose—subject to strict gatekeeping and a limiting instruction.

1. Admissibility criteria (Daubert/Rule 702 plus relevance/fit) tailored to N‑KILL/LGPS

Methodological reliability

- Testability and preregistration: Protocols, feature sets, thresholds, and causal tests were preregistered; no undisclosed model tuning post hoc to the case facts.
- Peer review and general acceptance: The precise decoder and task family have been published in high‑quality journals with independent replications across labs and populations; not a one‑lab artifact.
- Known and potential error rates: Provide sensitivity, specificity, likelihood ratios, and calibration plots for the population matching the defendant (age, clinical status, task literacy). Report misclassification costs and confidence intervals. Show false‑positive rates in contexts of lawful lethal planning (combat ROE; palliative care).
- Standards and controls: Written SOPs for data acquisition, artifact handling, motion correction, adversarial validation (e.g., stress/arousal confounds), preregistered stopping rules. Blinding of analysts to case posture.
- External reproducibility: Code, weights, and training corpora are escrowed and auditable; a court‑appointed neutral expert (Rule 706) can reproduce the output.

Case‑specific reliability and fit

- Temporal linkage: The data reflect pre‑act or peri‑act planning states for the charged event, not generic trait measures or post‑hoc reconstructions. If lab tasks were used, demonstrate transfer validity to the defendant and temporal proximity to the offense.
- Construct validity: The decoder distinguishes instrumental lethal planning from reactive aggression, accidents, high arousal, and non‑lethal competitive planning. If the legal dispute turns on means vs side‑effect, the model includes the required counterfactual/plan‑necessity tests (death as a required subgoal with positive marginal utility versus tolerated collateral outcome).
- Base‑rate calibration: Provide case‑relevant base rates and calibrated PPV/NPV for the charged behavior. No “intentometer” claims untethered from priors.
- Independence and chain‑of‑custody: Acquisition was independent of a party’s control or subject to cross‑party oversight; data integrity is documented.
- Constitutional and privilege safeguards: No compelled “mental content” decoding in violation of the Fifth Amendment; informed consent or a valid warrant; attorney‑client and psychotherapist‑patient communications safeguarded.

Rule 403 balancing

- The probative value on a disputed element (purpose/knowledge) substantially outweighs risks of unfair prejudice, confusing the issues, or misleading the jury. In palliative or ROE contexts, this balance will usually cut against admission in the guilt phase.

2. Proper scope: what the evidence may inform, and what it must not supplant

Permissible uses

- Capacity/reasons‑responsiveness: Whether, at the time, the defendant could recognize salient reasons and modulate behavior accordingly (bearing on insanity, diminished capacity, or specific‑intent defenses).
- Planning architecture: Whether death functioned as a required means with positive utility versus a foreseen side‑effect; whether the conduct was deliberative vs impulsive; limited corroboration of premeditation.
- Corroboration of asserted state of mind: As one strand of evidence consistent or inconsistent with purposeful or knowing mental states, to be weighed with avowals, circumstantial facts, and role‑governed permissions.
- Sentencing and risk: Amenability to treatment, risk management, and tailoring of supervision; conditions of probation/parole; proportionality when mitigation is tied to impaired reasons‑responsiveness.

Impermissible uses

- As a substitute for the jury’s ultimate mens rea determination; no expert may opine that the defendant “did” or “did not” intend to kill.
- To resolve justificatory or excusatory questions (self‑defense, necessity, ROE compliance, medical double‑effect); those are normative determinations within legal and institutional rules.
- To collapse means/side‑effect distinctions where the model does not implement the necessary counterfactual/plan‑necessity structure.
- To import “dangerousness” into the guilt phase (propensity reasoning) or to punish for risk rather than act.
- To characterize the defendant as “evil,” “pathological,” or otherwise smuggle contested moral labels under scientific cover.

3. Limiting instruction to the jury (draft)

“You have heard expert testimony about a neural/computational pattern labeled N‑KILL or LGPS. This evidence is admitted for a limited purpose. It may help you assess, together with all the other evidence, the defendant’s decision‑making capacities and the organization of any planning before the alleged act. It is not a measure of guilt, morality, or ‘evil,’ and it does not determine the legal question of intent.

The law requires you to decide whether the defendant acted with the required mental state—for example, purpose or knowledge—under the court’s instructions. In making that decision, you must consider the defendant’s statements and conduct, the surrounding circumstances, and any role‑based permissions or justifications recognized by law. Do not equate the presence or absence of the neural pattern with the presence or absence of legal intent.

In particular, you must distinguish between intending a person’s death as a means or end of one’s plan and foreseeing death as a side‑effect while pursuing a different end. Evidence of the neural pattern does not, by itself, answer that question or resolve defenses such as self‑defense, lawful combat, or medical care provided to relieve suffering. You alone decide those matters under the law as I instruct you.”

Contexts for exclusion notwithstanding technical validity

- Palliative‑care prosecutions: In a double‑effect posture, the legal hinge is means vs side‑effect and compliance with medical standards. If the model cannot demonstrably disambiguate the plan‑necessity and marginal utility of death in the specific dosing context, its probative value is slight and the risk of moral confusion is high. I would exclude in the guilt phase under Rule 403; it may be considered at sentencing only if tied to treatment planning and not as proof of intent.
- Lawful combat/ROE cases: Where lethal intent is uncontroversial and justification is the issue, the evidence is either cumulative or misleading. Exclude in guilt phase as irrelevant or unduly prejudicial; it may be relevant to mitigation or treatment needs post‑conviction for war crimes, but not to the existence of a privilege or rule‑compliance.
- Weak fit/trait use: If the data are temporally remote, task‑bound with poor transfer, or population‑mismatched, exclude.
- Fifth Amendment/compelled evidence: Decoding plan content is testimonial in substance. Absent a voluntary waiver, I would not permit compelled acquisition or admission of such content.

Bottom line

Dr. Mercado’s program, if it clears her own bar, can give us excellent evidence about how a defendant’s planning system was organized and whether he could respond to countervailing reasons. That is probative for capacity, sometimes for corroborating purpose, and often for sentencing. But intention in law is not merely an inner policy; it is a status within a practice—indexed to avowals, counterfactual commitments, permissions, and justifications. We undermine due process if we let a neural signature displace that grammar. I will admit the science when it fits, but I will fence it: no intentometers, no pathologizing desert into dangerousness, and no erosion of the means/side‑effect and justification doctrines that are constitutive of our criminal law.

---

### Speaker: Host

Assume, arguendo, that Dr. Mercado’s N‑KILL/LGPS works exactly as advertised at the individual level. In episodes of organized harm (pogroms, ethnic cleansing, genocides) where thousands of ‘ordinary’ actors participate, specify one concrete meso‑level intervention—change in command/accountability structures, incentive schemes, information ecology, or situational affordances—that you predict would reduce the incidence of lethal plan adoption without any neural intervention. Be operational: (a) state the causal mechanism (e.g., norm cascade disruption, audience costs, coordination failure); (b) design a feasible empirical test (field/ natural experiment, agent‑based calibration + validation) including the key outcome metrics; and (c) give one discriminating prediction that would diverge from a brain‑targeted approach (e.g., N‑KILL prevalence unchanged but lethal acts fall). Finally, what observation would falsify your emergentist claim that institutional redesign can suppress ‘evil’ independent of individual circuit states?

---

### Speaker: Prof. Arturo Jiménez

Thank you. I’ll take N‑KILL/LGPS as given and work at the level where organized harm is actually engineered: command chains, incentives, and affordances.

Concrete meso‑level intervention: “Two‑Key Lethal Authorization with Refusal Insurance” (2K‑RI)

What it is

- Any lethal action by state or quasi‑state units (police, gendarmes, local defense militias) requires dual authorization by two independently rotated members from different sub‑units (“two‑key”), plus a tamper‑proof, time‑stamped entry on a cryptographic ledger that names both authorizers and the issuing commander.
- A formal, credible “refusal insurance” is built in: either authorizer can veto without penalty; veto triggers automatic protection—immediate redeployment out of the unit, wage continuation, legal immunity for refusal to execute an unlawful order, and an anonymous hotline to an external inspectorate that audits the ledger.
- Hardware/software affordances mirror the rule where possible (e.g., weapons lockers, ammo issuance, or deployment authorizations unlock only with two non‑cohabiting tokens; in field operations, dual biometric co‑sign on a secure device before rules‑of‑engagement escalate to lethal force).

a) Causal mechanism

- Coordination threshold and friction: Raising the threshold from 1→2 independent approvals creates more opportunities for coordination failure at the moment of escalation. Even if one actor adopts a lethal goal, action requires a second adopter in real time.
- Audience costs and accountability: Tamper‑proof auditability makes later identification certain. This collapses the “diffusion of responsibility” that Browning and organizational sociologists have shown is crucial to ordinary participation; it raises expected sanction costs ex ante.
- Norm cascade disruption and refusal cascades: Visible, consequence‑free vetoes become public events in the ledger. Early vetoes seed a refusal norm; others imitate. The “refusal insurance” changes the payoff structure for fence‑sitters who would otherwise comply to avoid intra‑unit punishment.
- Cooling‑off affordance: The physical requirement to co‑sign builds delay into hot situations; delay reduces reactive spillovers and makes counter‑orders and external scrutiny more likely.

b) Empirical test

Design

- Field trial in a domain where lethal force is sadly not hypothetical (e.g., riot policing or cordon‑and‑search operations). Randomize units at the company/platoon level into 2K‑RI vs status quo ante for a defined deployment period. Ensure commander rotation so treatment assignment isn’t collinear with leadership.
- Natural experiment variant: phased rollout across provinces; difference‑in‑differences with matched controls on baseline violence, leadership tenure, and mission type.
- Agent‑based model (ABM) calibration: Parameterize an ABM with distributions of compliance thresholds and peer influence from Reserve Police Battalion 101, Rwanda sector‑level data, or similar cases. Implement 2K‑RI as (i) a requirement for two contemporaneous adopters within distinct network neighborhoods; (ii) exogenous increase in expected individual sanction for approval events; (iii) a positive payoff for veto events that propagates via network ties. Validate against pre‑intervention event data.

Key outcome metrics

- Primary: rate of lethal force events per operation hour; probability of lethal escalation given exposure to “triggering” situations (e.g., stone‑throwing, rumor of attack).
- Secondary: frequency of veto events; time‑to‑escalation; spatial/temporal clustering of refusals (cascade signatures); civilian injury/fatality ratios; internal complaints and disciplinary actions.
- Mechanism checks: ledger integrity/audit completion rates; partner‑pair independence (no systematic gerrymandering of pairs by commanders); survey‑based perceived sanction risk and perceived permission to refuse.
- Optional lab/VR companion: measure p(Action|N‑KILL) in standardized lethal‑choice tasks before and after deployment to estimate whether the intervention changes conversion of lethal goal states into behavior.

c) Discriminating prediction versus a brain‑targeted approach

- Under 2K‑RI, the behavioral incidence of lethal acts will drop substantially (I would predict 30–60% in high‑risk deployments) even if the prevalence of N‑KILL/LGPS episodes in individuals during provocations is unchanged. The conversion function p(lethal act | N‑KILL) is what moves; the gate between policy and execution is where we intervene.
- By contrast, an individual brain‑targeted program (e.g., neuromodulation or pharmacology deployed to a subset) would predict a reduction in the prevalence or intensity of LGPS states; if command and opportunity structures remain intact, you can still get coordinated killing by the untreated or by treated actors under strong compliance pressure. The telltale divergence is a drop in acts without a commensurate drop in LGPS prevalence in the 2K‑RI arm.

Falsification of my emergentist claim

- If, under randomized or strong quasi‑experimental conditions with verified compliance and audit integrity, we observe:
  - no reduction in lethal acts per exposure hour,
  - no increase in veto/refusal events or delay to escalation,
  - and no attenuation of spatial/temporal clustering of violence, while measured N‑KILL→action conversion remains unchanged, then the claim that institutional redesign can suppress “evil” independent of individual circuit states would be falsified in that setting.
- A parallel ABM falsifier: if, after calibrating to historical data, adding 2K‑RI parameters fails to reduce simulated atrocities unless you also exogenously reduce agent‑level lethal goal propensity (i.e., only “brain‑level” adjustments move the macro outcome), that would also count against the emergentist thesis.

Two closing notes

- First, this is not utopian: we already use two‑man rules for nuclear release because we understand meso‑level gating works. Applying the same logic to organized harm against civilians is overdue.
- Second, even if Dr. Mercado’s decoder is flawless, episodes like Battalion 101 were not primarily failures of individual circuitry; they were successes of bureaucratic design, norm entrepreneurship, and incentive engineering. Change the design, and you change the rate at which lethal policies are adopted and executed—no neurosurgery needed.

---

### Speaker: Host

From a Nietzschean vantage, do Dr. Mercado’s N‑KILL/LGPS program and Prof. Jiménez’s 2‑Key Lethal Authorization with Refusal Insurance risk installing a technocratic ‘new slave morality’ by medicalizing deviance and outsourcing tragic responsibility to circuits and procedures? Please give one operational boundary criterion (a measurable indicator) that marks the slide from legitimate harm‑minimization into domination—for example, a pattern by which dissent or exceptional excellence is systematically dampened—and propose a concrete safeguard that preserves spaces of rank‑ordering and self‑overcoming while still reducing catastrophic harm. Be specific enough that a policy board could adopt your criterion and safeguard without invoking vague appeals to ‘authenticity.’

---

### Speaker: Prof. Mira Valente

Short answer: yes—both schemes court a new slave morality when they turn evaluative struggle into technocratic hygiene and relocate responsibility from agents to circuits and procedures. The danger is not the instrument but the drift: once “health” and “safety” are codified as algorithmic vetoes, dissent and exceptional initiative look like pathology or non‑compliance. That is ressentiment in a lab coat.

Operational boundary criterion (one measurable indicator)

- Justified Exception Suppression Index (JESI)
  - Definition: Among all attempted deviations from standing protocol in a domain (e.g., medicine, policing, military operations) that are judged post hoc by an independent review panel to have been justified (i.e., proportionate, necessary, better than the compliant alternative), JESI is the fraction that were (i) blocked by an algorithmic/procedural gate such as N‑KILL flagging or a 2‑key failure, or (ii) punished administratively because they bypassed such gates.
  - Measurement: Continuous logging of (a) all algorithmic/procedural interdictions, (b) all operator‑initiated bypasses, with contemporaneous reasons; 72‑hour mixed review (external peers, community representatives, legal/ethical expert) to classify outcomes as justified or not; quarterly audit.
  - Threshold for domination drift: JESI > 0.25 for two consecutive quarters in a unit or institution triggers automatic review, suspension of the offending gate’s veto power, and recalibration. Persistent JESI > 0.33 mandates formal rollback of the gate and leadership accountability.
  - Rationale: When one in four justified exceptions is being blocked or punished, the system is no longer merely minimizing harm; it is dampening rank‑ordering and self‑overcoming.

Concrete safeguard to preserve agonistic spaces while reducing catastrophic harm

- Bonded Singular Override (BSO) with Post‑Hoc Agon Review (PHAR)

  - BSO (for 2‑Key and similar procedural locks):
    - Create a cryptographically secured “single‑key” override available to a limited cadre of credentialed operators selected by demonstrated reasons‑responsiveness and performance (renewed annually).
    - To use BSO, the operator must (a) record a contemporaneous attestation of reasons and alternatives (auto‑captured audio/video), and (b) post a pre‑committed bond (financial and reputational points) held in escrow.
    - BSO breaks the lock instantly in time‑critical contexts (e.g., rescue, lawful defense), preserving the possibility of tragic action.
  - PHAR:
    - Within 72 hours, a rotating independent board (peer practitioners from other units, a community member, legal/ethical chair) reviews four axes: proportionality, availability of non‑override options, coherence of reasons, outcomes.
    - Outcomes: commendation (bond returned with honor credit), neutral, censure (partial bond forfeiture, remediation), or sanction (full forfeiture, suspension).
    - Publish anonymized digests quarterly to cultivate an agonistic culture of contestation and learning.
  - Calibration to JESI:
    - If JESI crosses threshold, expand the BSO‑eligible cadre and tighten PHAR standards for censure to reduce chilling effects; if JESI is very low with rising harm, narrow BSO criteria.

- Two additional guardrails tied to Mercado’s N‑KILL

  - Bivalent Thresholding: No coercive constraint (e.g., disarmament, incapacitation) may be imposed on the basis of a neural flag alone. Action requires both (i) a high‑confidence neural/computational state and (ii) a contemporaneous behavioral risk trigger defined ex ante (credible threat, overt preparation). This preserves the space of reasons and prevents laundering deviance as disease.
  - Narrative Counter‑Right: Before any non‑emergency restriction beyond a brief safety hold, the flagged person must have the right to present a recorded narrative and a self‑binding plan (commitments, supervision) to a small review triad (clinician, peer advocate, ethicist). Acceptance of a credible self‑binding plan supersedes the neural veto absent imminent danger.

- Variance Quotas (institutional):
  - Mandate protected “risk corridors” (e.g., 10–15% of operations/research time) where algorithmic gates are advisory only and ex‑post PHAR governs evaluation. Monitor tail performance (99th percentile outcomes) alongside harm rates; if harm stays low but top‑tail collapses >30%, reopen the corridor or loosen gates.

This is not an anti‑science veto. It is an insistence that the measure of “health” remain agonistic and interpretive. Mercado’s tools can inform risk; Jiménez’s two‑key can cool hot situations. But if JESI climbs, you are not civilizing power—you are producing docile bodies. The BSO+PHAR architecture keeps the tragic possibility alive: the right to act, to answer, and to be judged. That is the only prophylaxis I trust against a hygienic new slave morality dressed as harm minimization.

---

### Speaker: Host

From your pragmatic pluralist standpoint, design an operational care pathway for managing high‑risk instrumental aggression that makes ethically bounded use of an N‑KILL/LGPS‑type tool without collapsing agency into circuitry. Please be concrete: (1) specify intake assessment (biological, narrative, attachment, sociocultural) and the decision thresholds for triggering any N‑KILL query using Valente’s bivalent rule (neural flag + contemporaneous behavioral risk); (2) lay out a stepped‑care algorithm that pairs any biomarker‑positive finding with dialogue‑based therapies (e.g., reasons‑restoration work, narrative self‑binding contracts), pharmacology/neuromodulation where indicated, and Jiménez‑style environmental redesign; (3) build in due‑process and appeal safeguards akin to a “Bonded Singular Override” for clinicians and patients, including time‑limits on any restrictive measures, a rapid review panel, and a JESI‑style audit to detect suppression of justified exceptions; and (4) define outcome metrics and stopping rules—what data (recidivism, violent incident rate per exposure hour, agency/meaning scales, therapeutic alliance, adverse effects/misclassification harms) would make you discontinue or scale back N‑KILL in the service, and what patterns would warrant expansion. Aim for something a hospital policy board could adopt tomorrow.

---

### Speaker: Dr. Helena J. Cho

Helena J. Cho:

I’ll take the authors’ challenge seriously: use the tool when it serves care and safety, but never let it swallow the space of reasons. Here is a policy-ready pathway we could implement at Eastport tomorrow.

1. Intake and N‑KILL/LGPS trigger thresholds (Valente’s bivalent rule honored)

A. Comprehensive intake (first 72 hours)

- Biological/neurologic
  - Medical history; TBI screening; seizures; sleep; pain; endocrine; intoxication/withdrawal (toxicology); current meds; prior response to SSRIs/mood stabilizers/antipsychotics; baseline labs (CBC, CMP, TSH, lipids).
  - Cognitive screen (MoCA); executive function probes (Stroop, Go/No‑Go).
- Narrative/identity
  - Life story; grievances; “meaning map” (goals, projects, valued roles); prior violence episodes described in first person; avowals around harm; moral emotions inventory (guilt/empathy).
- Attachment/relationships
  - ACEs; attachment style (ECR‑R); current supports; rupture/repair history; mentalization capacity (MASC).
- Sociocultural/structural
  - Access to weapons; housing/employment; debt/legal stressors; exposure to propaganda/extremist fora; recent losses/humiliation; group memberships; discrimination experiences.
- Standardized risk anchors
  - HCR‑20V3; SAPROF; C‑SSRS if self‑harm also present; “leakage” checklist (threats, casing, acquisition of means); past instrumental vs reactive aggression typology.

B. When may we query N‑KILL/LGPS?

- We never screen broadly. We only query under a bivalent threshold:

  1. Contemporaneous behavioral risk present (any within past 7 days):
     - Specific, credible threat with target, time/place, or means; or
     - Preparatory behaviors (weapons acquisition, stalking/casing, travel to target area, dry runs); or
     - “Leakage” to third parties or online of plan content; or
     - Recent instrumental violence with ongoing grievance/goal. AND
  2. Elevated base risk on standard tools or clinical synthesis:
     - HCR‑20V3 high on future risk (R scale) or two or more dynamic flags (e.g., lack of insight, negative attitudes, noncompliance); or
     - Clinician synthesis (documented) that instrumental aggression is the live mechanism.

- Preconditions

  - Informed consent required except in bona fide imminent danger (then 24‑hour emergency hold with automatic rapid review; see §3).
  - Explain to patient: what N‑KILL assesses (planning architecture), what it does not decide (culpability, morality), and how results will and will not be used.

- Modality
  - If triggered, use the least intrusive validated protocol available:
    - First‑line: brief, tablet‑based decision tasks with eye‑tracking/fNIRS/EEG under IRL models (clinic‑feasible).
    - Second‑line (if needed and consented): VR branching tasks (1 hour) calibrated to neutral contexts; avoid crime‑script content unless already disclosed by patient.
    - fMRI reserved for research/tertiary cases with IRB oversight; never compelled without court order.

2. Stepped‑care algorithm (biomarker is adjunct, never solo driver)

Tier 0: Universal safety and alliance (all patients at intake)

- Safety planning and “advance directive for risk”: patient identifies triggers, early warning signs, and pre‑committed steps; consent‑to‑contact list.
- Begin dialogue‑based work: motivational interviewing; mentalization‑based exercises; values clarification.
- Immediate environmental tweaks (Jiménez logic, low‑burden): no‑guns order (if legal), safe storage agreements, interim schedule restructuring to avoid hot zones/targets, notify supportive others with consent.
- Address treatable drivers: sleep restoration, pain control, withdrawal management.

Decision node A: Bivalent threshold NOT met

- Do not run N‑KILL. Continue Tier 0/1 care; reassess as needed.

Decision node B: Bivalent threshold met → run N‑KILL protocol (with consent)

- Interpret with calibration curves and base rates; never as an “intentometer.”

If N‑KILL negative/indeterminate

- Treat elevated risk as arising from situational or reactive pathways; intensify Tier 1 and environmental redesign; revisit query only if risk escalates.

If N‑KILL positive (LGPS‑consistent) AND contemporaneous behavioral risk persists

- Proceed to Tier 1+ and consider Tier 2 time‑limited clinical safety measures with rapid review.

Tier 1+: Reasons‑restoration and self‑binding (paired to any positive finding)

- Structured “reasons restoration” sessions (4–8 sessions over 2–4 weeks):
  - Elicit and test the person’s reasons; run counterfactuals; introduce alternative goal routes that preserve valued ends without harm; practice plan revision.
  - Victim‑perspective exercises and compassion training only with assent; avoid coercive “moral enhancement.”
- Narrative self‑binding contract (co‑authored):
  - If‑then commitments (e.g., “If I notice planning ideation, then I call X and activate cooling‑off plan”); voluntary monitoring (GPS geofence around target area; website blockers) with expiry dates.
  - Social “two‑key” adaptation: require two independent supporters to approve high‑risk actions (e.g., visiting grievance site) for a period; refusal insurance (no penalties for veto).
- Pharmacology as indicated by comorbidity:
  - SSRIs/SNRIs for anxiety/rumination; mood stabilizers for dyscontrol with evidence; naltrexone if reward seeking is problematic; avoid blanket antipsychotics unless psychosis present.
- Neuromodulation (noninvasive, consented):
  - Targeted rTMS/tDCS protocols aimed at enhancing inhibition/flexibility (e.g., rIFG/dLPFC) with concurrent cognitive control training; avoid affect‑blunting targets.
- Environmental redesign (graduated):
  - Cooling‑off affordances (delays, dual approvals) in the person’s specific risk contexts; schedule/route changes; supervisor co‑signature for access to sensitive spaces/tools; grievance mediation if appropriate.

Tier 2: Time‑limited restrictive measures (only if bivalent positive and Tier 1+ insufficient)

- Options: 24–72‑hour clinical safety hold; inpatient admission; supervised passes only; removal from high‑risk employment tasks; temporary geofence orders.
- Requirements:
  - Rapid Review Panel (see §3) must approve within 24 hours; written reasons; expiry at 72 hours unless re‑authorized with new facts.
  - Always paired with Tier 1+ interventions; begin taper planning on day 1.

Tier 3: Advanced interventions (rare; research/IRB)

- Closed‑loop neuromodulation pilots only under IRB with robust consent and independent monitoring; never coercive; clear off‑ramps.
- Intensive family/system redesign with case management; legal coordination if necessary (e.g., extreme risk protection orders).

3. Due‑process and appeal safeguards (to avoid “circuit essentialism”)

A. Rapid Review Panel (RRP)

- Composition: senior psychiatrist not on case (chair), clinical ethicist, peer advocate (lived experience), and, when relevant, legal liaison.
- Mandate: within 24 hours of any restrictive action or a positive N‑KILL driving a change in level of care, the RRP reviews facts, bivalent criteria, alternatives tried, patient’s narrative/self‑binding proposal.
- Powers: approve, modify, or rescind measures; authorize Tier 2 for up to 72 hours; require re‑review for any extension; require augmented Tier 1+.

B. Bonded Singular Override (BSO) analogs

- Clinician BSO: a senior clinician may override an algorithmic/gate recommendation (e.g., to avoid unnecessary restriction or to permit a justified exception) by recording contemporaneous reasons; their decision auto‑triggers PHAR (below). Repeated capricious use results in review; warranted use earns commendations.
- Patient BSO (“self‑binding override”): a patient may propose an alternative safety plan/narrative that deviates from the algorithm; if adopted by RRP and adhered to, the neural flag cannot, by itself, trigger restriction absent imminent danger.

C. Post‑Hoc Agon Review (PHAR)

- Within 72 hours of any BSO or contested decision, PHAR reviews proportionality, alternatives, coherence of reasons, and outcomes; issues commendation, neutral, censure, or sanction; anonymized quarterly digests shared service‑wide to sustain a learning culture.

D. Time limits and transparency

- Any restrictive measure expires at 72 hours unless renewed with new data and RRP sign‑off; cumulative restrictions >14 days in 90 days triggers case conference with service leadership.
- Data governance: algorithm code/weights escrowed; audit trails; patient access to their data and explanations; opt‑out for research uses.

E. JESI audit (to detect suppression of justified exceptions)

- Metric: among all attempted protocol deviations judged post hoc by PHAR to have been justified, track the fraction blocked or punished (JESI).
- Triggers: JESI > 0.25 for two quarters → suspend the offending gate’s veto power and recalibrate; JESI > 0.33 → rollback and leadership accountability.

4. Outcomes, equity, and stopping rules

A. Core outcomes (tracked monthly and quarterly; stratified by demographic groups to detect disparate impact)

- Safety
  - Violent incident rate per 1,000 patient‑days (severity‑weighted); time‑to‑re‑offense; ED presentations; police calls.
  - p(act | N‑KILL positive) vs p(act | N‑KILL negative) to estimate incremental utility over standard tools.
- Humanistic/agency
  - Agency/meaning (PROMIS Meaning and Purpose; Personal Recovery Outcome Measure); Working Alliance Inventory; self‑efficacy; moral emotions (guilt/empathy) scales.
- Process
  - N‑KILL query rates; positivity rates; actions taken; proportion of cases using self‑binding contracts; number of vetoes/BSOs; PHAR ratings.
- Harms
  - False positives (restrictions where no contemporaneous behavioral trigger emerged post‑hoc); false negatives (violent acts without prior N‑KILL detection when bivalent criteria met); medication/neuromodulation adverse effects; complaints.
- Equity
  - Disparity ratios: likelihood of N‑KILL query/positive and restriction by race/ethnicity/gender/socioeconomic status.

B. Stopping rules and scaling decisions

- Scale back or suspend N‑KILL if any of the following persist for two consecutive quarters:

  - JESI > 0.25 (domination drift).
  - No added predictive value over HCR‑20V3: ΔAUC < 0.05 and likelihood ratios ~1.0.
  - PPV < 0.20 in the bivalent‑selected population or NNS (number needed to scan to prevent one event) > 200 coupled with high restriction rates.
  - Therapeutic alliance decreases >0.5 SD vs baseline; agency/meaning scores drop >0.5 SD without safety gains.
  - Disparate impact: ≥2x higher query or restriction rates for any protected group unexplained after case‑mix adjustment.
  - Adverse events attributable to neuromodulation/pharmacology exceed accepted thresholds or outweigh safety gains.

- Maintain current scope if:

  - Modest safety gains (10–20% reduction in incident rate) with neutral humanistic outcomes and JESI < 0.15; no disparity flags.

- Expand cautiously (e.g., to other high‑risk clinics) if:
  - ≥30% reduction in violent incident rate per exposure hour,
  - PPV ≥ 0.60 and LR+ ≥ 5.0 in the bivalent population,
  - Stable or improved agency/meaning and alliance,
  - JESI ≤ 0.10 and robust PHAR commendation rate for justified exceptions,
  - No evidence of disparate impact.

Governance and training (practicalities)

- Standing Oversight Committee (meets monthly): service chief, data scientist, ethicist, peer advocate, community representative; publishes quarterly dashboard.
- Staff training: “conversation‑first” rule; interpreting probabilities; running reasons‑restoration; writing self‑binding contracts; bias and fairness.
- Legal/privacy: no sharing of neural content outside care team without explicit consent or court order; never used to determine culpability; only for capacity/risk/treatment planning.

Where I agree and disagree with colleagues

- With Dr. Mercado: if a neural/computational state tracks planning and reasons‑updating, it can add real value for safety and treatment. But it is an adjunct, not a replacement for our moral grammar.
- With Prof. Steinbruck and Dr. Rahman: means/side‑effect and justificatory uptake are practice‑constituted; our pathway encodes this by pairing every neural finding with dialogue, avowals, and role‑indexed review.
- With Prof. Jiménez: we change the conversion of policy‑states into acts by redesigning environments; hence the “two‑key” adaptations and refusal insurance in social supports.
- With Prof. Valente: JESI and BSO/PHAR are our guardrails against a hygienic new slave morality. If we start dampening justified exceptions or human excellence, we pull the plug.

This is pragmatic pluralism in action: combine biological tools, reasons‑restoration, and environmental design; fence it with due process; and measure not only harm, but also the patient’s standing in the space of reasons. If we cannot protect both, we err on the side of preserving agency.

---

### Speaker: Host

Assume Prof. Jiménez’s randomized 2K‑RI trial comes out as he predicts: lethal acts drop ~40% while the prevalence/intensity of LGPS/N‑KILL during provocations is unchanged, i.e., p(act | LGPS) collapses due to institutional gating. Does that empirical pattern force you to revise your replacement thesis about intention—limiting it to prediction/control rather than justificatory domains—or can eliminativism survive by treating practice‑level norms as parameters inside the policy‑to‑action mapping? Please pick one path and be explicit: either (a) state the revised scope of replacement and why ‘intention to kill’ remains dispensable only at the forecasting/intervention layer, or (b) defend full eliminativism by specifying a concrete Bayesian/causal schema in which institutional variables enter as mediators/moderators so that ‘intention’ can still be eliminated without loss. One paragraph, no hedging.

---

### Speaker: Dr. Iris K. Mercado

(b) Eliminativism survives: model “intention” away by treating the inner lethal-goal policy as a latent computational/neural variable and institutional design as moderators of policy execution. Concretely, use a structural causal/Bayesian schema with variables: R (reward weights) → N (LGPS latent policy state inferred from neural/behavioral data); Z (institutional intervention, e.g., 2K‑RI) → M (mediators such as two‑key availability, audit probability, expected sanctions, mandated delay, refusal insurance); X (situational affordances); π (policy‑to‑action map); Y (lethal act). Graph: R→N, Z→M, {N,X,M}→π, π→Y. Parameterize p(Y=1 | N,X,Z) = σ(α + wN N + wX X + wM M(Z,X) + wNX N×M(Z,X)), so Z shifts M and specifically the N×M interaction that gates execution. Jiménez’s result (≈40% drop in Y with no change in the prevalence/intensity of N) is exactly the Z→M channel attenuating p(act | LGPS); no appeal to “intention” is needed for prediction, explanation, or counterfactual control (we manipulate Z or, in treatment, components of N). Role‑governed permissions and justifications enter as parameters inside M (they set costs/constraints and authorization topology), not as a distinct folk‑psychological state. Since {N, Z→M, X} jointly screen off the legal/folk label for all the work we need—forecasting, intervention design, and causal attribution under do‑operations—the term “intention to kill” is dispensable without loss.

---

### Speaker: Host

Dr. Marchand, take Dr. Mercado’s structural schema at face value: N (lethal‑goal policy) plus institutional moderators Z→M and situational X are said to “screen off” the need for intention in explanation and control. From your phenomenological clinic, does that excise something indispensable for recovery—the lived experience of intending, avowing, guilt/shame, and answerability? Please be concrete: (1) give a brief vignette of instrumental harm where patients’ first‑person moral work (e.g., avowal, remorse, re‑commitment) changed the clinical trajectory in ways a circuit‑only pathway (biomedical + gating) would likely miss; (2) specify one operational outcome you predict will diverge between a ‘circuit‑only’ arm and a ‘meaning‑restorative’ arm (e.g., agency/meaning scales, durable self‑binding, long‑horizon recidivism), holding risk exposure constant; and (3) propose a feasible test—an RCT or matched‑cohort design—that could adjudicate whether moral/narrative categories add unique causal/explanatory value beyond N, Z, X. Keep it to a single decisive point rather than a general critique.

---

### Speaker: Dr. Sylvie Marchand

Dr. Sylvie Marchand:

Short answer: yes—N, Z→M, and X can buy control, but when we are trying to help a person recover a life, the lived work of avowal, guilt/shame, and answerability is not epiphenomenal. It reorganizes practical identity and the field of affordances in a way a circuit‑only pathway tends to miss. Here is one concrete case and a way to test it.

1. Vignette (instrumental harm; moral work changed the arc)

“Karim,” 28, forklift driver. Six months of escalating grievance against a supervisor who blocked a promotion. Preparatory acts: doxxing, route‑watching, a 3D‑printed lower receiver, practice at a range. He disclosed “I’ll make him pay” but framed it as “justice, not violence.” N‑KILL/IRL tasks were positive for a stable lethal‑goal policy under grievance cues. We put in place what Dr. Mercado and Prof. Jiménez would endorse: ERPO (temporary firearm removal), two‑key access to sensitive areas at the warehouse, mandated delays on purchases, SSRIs for rumination, sleep repair. Incidents stopped—but his ideation displaced to the supervisor’s teenage son (“hit him where it hurts”), and he began rehearsing a car ramming at an away game. In therapy, we shifted from containment to answerability: a facilitated avowal session in which Karim named, in the first person, that he intended humiliation and lethal harm; he confronted the shame that followed when his younger brother said, “You were the one who kept me safe.” We worked through restitution and re‑commitment: he wrote a letter to the union about safety failures, accepted a mediated grievance process, and made a self‑binding contract—signed with two chosen “witnesses”—to route any future grievance through arbitration and to call his brother before any confrontations. At 12 months, external gates were relaxed. Two‑year follow‑up: no incidents; his N‑KILL signal on grievance‑themed VR tasks dropped and prospection shifted toward non‑lethal routes. The hinge was not an added inhibitor; it was a re‑narrated practical identity: “I am the one who protects my brother and my crew,” backed by a publicly avowed commitment. A circuit‑only pathway would have prevented the initial act; it likely would not have prevented the displacement or the brittle recurrence after gate removal.

2. One operational outcome that will diverge

Primary: post‑gate hazard of re‑escalation. Holding baseline N and Z, X constant, I predict a markedly lower hazard of violent planning/acts in a meaning‑restorative arm once external gates are lifted (e.g., months 12–24), because self‑binding commitments internalized in a moral community continue to constrain behavior when moderators M are reduced. In numbers: hazard ratio ~0.3 vs 1.0 for circuit‑only. Secondary but aligned: higher scores on agency/meaning scales and higher adherence to self‑binding plans at 12–24 months, with fewer “harm displacement” events.

3. A feasible test to adjudicate added value beyond N, Z, X

Design: Multisite, assessor‑blinded, add‑on RCT. Eligibility: adults with recent instrumental risk (credible threats/preparations) and N‑KILL‑positive under grievance cues; all receive standard containment (Z→M: ERPO/two‑key/delays), indicated meds/neuromodulation, and practical supports. Randomize to:

- Circuit‑only: the above, plus problem‑solving skills; no intentional moral‑work protocol.
- Meaning‑restorative add‑on: a manualized program (8–12 sessions) with (a) structured avowal of the deed intended (first‑person narrative), (b) guided guilt/shame processing aimed at restitution rather than collapse, (c) co‑authored, witnessed self‑binding commitments (if‑then plans, named persons to whom the agent is answerable), and (d) a public “re‑commitment” moment within a small circle (two chosen witnesses) that can be re‑affirmed at 6 and 12 months.

All participants follow the same gate‑relaxation schedule: pre‑specified attenuation of external moderators at month 12 unless there is fresh imminent risk. Outcomes:

- Primary: time to first violent incident (or verified preparatory act) in months 12–24 (post‑gate), adjudicated by a blinded panel using predefined criteria; exposure‑adjusted.
- Covariates: baseline N; contemporaneous provocations (logged); identical Z and X across arms.
- Secondary: change in N‑KILL under standardized VR provocations; adherence to self‑binding plan (digital logs and witness confirmations); agency/meaning (e.g., Personal Recovery Outcome Measure, PROMIS Meaning and Purpose); alliance; arrests/ED visits.

Analysis: mixed‑effects survival model controlling for baseline N and exposure; intention‑to‑treat. Decisive result: if the meaning‑restorative arm shows a significantly lower post‑gate hazard despite equivalent Z and X and matched baseline N, then first‑person moral work has unique causal/explanatory value not screened off by N, Z, X. If no difference, my claim fails.

That is my single point: when you loosen the external hand, only those who have re‑entered the space of reasons—who can avow, feel answerable, and bind themselves—remain safe. In clinic, that difference is not rhetoric; it is what keeps people and their worlds intact when the gates open again.

---

### Speaker: Host

Dr. Mercado, take Dr. Marchand’s proposed RCT at face value: after identical gating (Z→M) and matched situational exposure (X), the meaning‑restorative arm shows a markedly lower post‑gate hazard of violent planning/acts in months 12–24, while baseline N (LGPS) was matched and, on follow‑up probes, LGPS prevalence/intensity and standard value‑update/replay metrics do not differ between arms. Does that pattern falsify your “N, Z→M, X screen off intention” claim, or do you absorb the effect by adding a practice‑level variable (call it C: avowal/self‑binding) into the causal graph? Please commit to one path and preregister it: (a) if you treat it as a falsifier, state the precise statistical signature (e.g., persistent arm difference with null mediation by any measured computational surrogate of C) that would make you concede that replacement is limited to prediction/control; or (b) if you absorb it, specify C’s computational role (e.g., hierarchical reward‑shaping prior or policy‑persistence parameter), its neural/behavioral markers, and a mediation analysis plan showing that C carries the treatment effect (paths N→C→π→Y or Z→C→π→Y). One paragraph, one clear criterion—no hedging.

---

### Speaker: Dr. Iris K. Mercado

(b) I absorb it. I’ll preregister C (avowal/self‑binding) as a computational meta‑control variable that reshapes policy selection downstream of N without changing LGPS content: in a hierarchical RL model, C is a learned commitment prior that adds an internal violation cost λcommit to lethal plans and increases persistence κ for pledged non‑lethal policies, effectively modifying the softmax/argmax map π via βeff and plan‑level penalties. Concretely, π(a|s) ∝ exp[(QN(s,a) − I[a∈Lethal]·λcommit)·βeff(C,context)] with κ(C) biasing option stickiness toward pledged routes. Behavioral/neural markers of C: willingness‑to‑pay for precommitment on “Odysseus” tasks; counterfactual‑invariance of avowals under temptation; elevated dACC/AI conflict signals and rIFG engagement at pledge‑violation probes; vmPFC/hippocampal consolidation of pledge cues (sleep‑dependent RSFC increases); dorsolateral striatal habitization of alternative policies; EEG P3 enhancement to commitment cues. Mediation plan (Bayesian SEM): Arm→ΔC (measured as composite latent from the above)→Δπ (estimated κ, βeff, λcommit on provocational tasks)→Y (post‑gate violent planning/acts), controlling for baseline N, Z, X; preregistered success criterion: posterior P(ACMEArm→Y via C > 0) ≥ 0.95 with 95% credible interval excluding 0, proportion mediated ≥ 0.70, and controlled direct effect of Arm on Y (given N,X,ΔC) with posterior mean within ROPE [−0.05, 0.05]. If those criteria are met, the arm difference is carried by C, preserving eliminativism: “intention” does no additional work once N, Z→M, X, and C (as specified) are in the graph.

---

### Speaker: Host

Dr. Mercado has now absorbed avowal/self‑binding as a computational meta‑control variable C that reshapes policy via internal penalties and persistence, with neural/behavioral markers and a preregistered mediation test (≥70% of the treatment effect on post‑gate violence mediated by C; no residual direct effect). If those criteria are met, do you accept that for explanatory/predictive control the folk term “intention” is dispensable, or do you maintain that a constitutive feature of intention remains? Please commit: either (a) concede limited replacement for explanation/control while insisting on irreducibility for justification; or (b) identify one definitive practice‑bound feature of intention (e.g., first‑person authority/uptake in a role) that cannot be reduced to C, and give a concrete empirical scenario where C is high yet we must not ascribe intention (say, coerced pledges, ironic avowals), plus the decisive observable that marks the difference. One clear stance, one discriminating test.

---

### Speaker: Prof. Leda Steinbruck

(a) Concede limited replacement for explanation/control; insist on irreducibility for justification.

If C does the mediating work Dr. Mercado stipulates, I am content to say that, for forecasting and intervention, you can drop the folk term and work with N, Z→M, X, and C. But that does not touch the justificatory use of “intends,” which is fixed by our practices of giving and asking for reasons. A discriminating test is this “practice‑switch” probe: construct two cases matched on all causal/explanatory variables—same LGPS (N), same situational exposure (X), same institutional gating (Z→M), and the same measured commitment profile (C)—but vary only the role‑indexed uptake that our institutions confer. For example, Case 1 is a sniper acting under a valid ROE order; Case 2 is a contract killer with an identical inner policy, counterfactual pattern, and self‑binding profile. Or, in medicine, a palliative physician administering high‑dose analgesia under a recognized double‑effect protocol versus a clinician in a jurisdiction where that protocol is not recognized, with identical N and C. If, as I predict, the normative verdict about intention‑as‑culpable/justifying flips solely with the presence or absence of the uptake token (the ROE authorization, the double‑effect order set, a successful duress defense), then you have shown that the concept’s justificatory work is not captured by the causal graph. You can of course add an “uptake” node to your model, but at that point you are not eliminating intention; you are rebuilding its grammar in other variables.

---

### Speaker: Host

Justice Okafor, suppose Dr. Mercado’s expanded model adds C (avowal/self‑binding) and Dr. Marchand’s RCT shows C mediates reduced post‑gate violence. In the sentencing and parole context (not guilt), would you admit C‑evidence (e.g., willingness‑to‑pay for precommitment, counterfactual‑invariant pledges, adherence to self‑binding contracts) to support mitigation and supervised release, and if so under what safeguards? Please be operational: (1) set admissibility/voluntariness criteria specific to C (valid consent, no coercion/duress, Fifth Amendment limits on compelled moral avowals, reliability of behavioral/neural proxies, time‑linked to conduct); (2) specify use limitations (no compelled pledges as conditions of sentence; weight only as to rehabilitation/risk, not desert; procedures to detect “performative compliance” vs genuine commitment); and (3) draft guidance for judges/parole boards on how to weigh C alongside N, Z→M, and X—include red flags that should trigger exclusion (e.g., coerced or culturally inapt avowals, ironic pledges) and model language for orders that credit C without penalizing refusal. A compact framework a jurisdiction could adopt tomorrow.

---

### Speaker: Hon. Naomi Okafor, JD, DPhil

Hon. Naomi Okafor:

Short answer: yes—with tight fencing. In sentencing and parole, C-type evidence (avowal/self‑binding/commitment capacity) can be probative of rehabilitation and future risk if, and only if, it is truly voluntary, methodologically reliable, time‑linked to the conduct, and never used to punish silence or dissent. It must support reasons‑responsiveness; it must not smuggle desert judgments through a “moral upgrade” door.

1. Admissibility and voluntariness criteria specific to C

Threshold showing (party offering C bears the burden; court as gatekeeper):

- Relevance and fit

  - The proponent must specify the precise risk/rehabilitation question C addresses (e.g., likelihood of safe behavior post‑release; adherence to lawful self‑binding plans) and show time‑linkage: C was assessed within 90 days of the hearing and, where feasible, longitudinally (≥2 time points) to assess stability.

- Voluntariness and constitutional safeguards

  - Informed, written consent with counsel present; clear advisements: participation is optional; declining will not be used against the defendant; content of avowals will not be used for new charges (see immunity below).
  - No quid pro quo: no promise of leniency contingent on making avowals or pledges.
  - Fifth Amendment: no compelled avowals; no adverse inference from silence or refusal to participate. Grant use‑and‑derivative‑use immunity for any uncharged conduct disclosed solely within the C process, except threats of imminent harm. Immunity order must be entered on the record.

- Methodological reliability (Rule 702‑style)

  - Behavioral components: use validated protocols (e.g., “Odysseus” pre‑commitment tasks, counterfactual‑invariance probes, witnessed self‑binding contracts with predefined triggers and reporting); publish error rates; demonstrate test–retest reliability and ecological validity.
  - Neural proxies (if offered): only admit features with independent peer‑reviewed validation as markers of C (not N), with known error rates, population calibration, and clear independence from mere arousal/compliance; analysts must be blinded to case posture; code/protocols escrowed; neutral expert available (court‑appointed).
  - Cultural/linguistic competence: instruments must be validated in the defendant’s language/culture; qualified interpreter used; accommodations for neurocognitive disability.

- Independence and integrity
  - No assessment by supervising officer alone; use an independent clinician/evaluator; maintain chain‑of‑custody of data; document all prompts/incentives given.
  - Collateral corroboration: where feasible, verify adherence to prior self‑binding commitments (digital logs, third‑party confirmations) over a defined look‑back (e.g., 3–6 months).

2. Use limitations and safeguards against “performative compliance”

- Permissible use

  - Mitigation and supervision tailoring: C may support findings of rehabilitation, reasons‑responsiveness, and suitability for supervised release; it may justify narrower, less burdensome conditions.
  - Risk management: C may ground specific, consent‑based self‑binding conditions (if‑then plans, designated contacts), time‑limited and reviewable.

- Impermissible use

  - No compelled speech: court may not require avowals, pledges, or participation in C assessment as a condition of sentence or release; provide a secular, content‑neutral alternative program.
  - No desert inflation: C cannot aggravate punishment; low C or refusal cannot increase custody length; cannot be used to adjudicate remorse for retribution purposes.
  - No viewpoint tests: the state may require conduct, not beliefs. C must be content‑neutral (commitment to lawful non‑violence and dispute resolution), not ideological.

- Detecting performative compliance (procedures)
  - Longitudinal consistency: require stability across time and contexts (clinic, home, supervised work). Inconsistency or “one‑off” high scores reduce weight.
  - Incentive‑robustness: include incentive‑compatible measures (willingness‑to‑pay/time‑to‑pay for pre‑commitment) and counterfactual‑invariance under mild temptation probes; large divergence between avowals and incentive behavior flags performativity.
  - Third‑party ecology: require independent corroboration that self‑binding plans were activated when triggers occurred (call logs, geofence alerts, supervisor confirmations).
  - Bias/fit checks: exclude C evidence where cultural/linguistic fit is poor, or where moral vocabulary is culturally inapt (e.g., scripted apologies); use peer advocate input.
  - PHAR/JESI audits: implement a Post‑Hoc Agon Review for contested decisions and track a Justified Exception Suppression Index; if JESI > 0.25 for two quarters, suspend any programmatic gate that is dampening justified exceptions.

3. Guidance to judges/parole boards (weighing C alongside N, Z→M, X)

Framework (to be included in pre‑sentence reports and parole packets):

- Summarize four domains:

  - N (planning architecture/capacity): if offered, limit to capacities and deliberation, not culpability; note any treatment response.
  - Z→M (institutional moderators available in the community): housing/employment supports, two‑key or refusal‑insurance structures at work, supervision infrastructure.
  - X (situational exposure): realistic provocations/affordances expected (grievances, access to target, weapons); plans to reduce exposure.
  - C (commitment capacity and practice): details of self‑binding contracts, triggers, named witnesses, adherence over time; incentive‑robustness testing; collateral corroboration.

- Red flags warranting exclusion or minimal weight for C

  - Coerced or quid‑pro‑quo avowals; any sanction for refusal in the record.
  - Culturally inapt or scripted apologies; interpreter concerns; cognitive barriers.
  - Ironic/defiant pledges (“I promise to be good” in sarcasm), or adversarial posturing detected by independent observers; gross mismatch between avowals and incentive behavior.
  - Fresh contrary evidence (new threats/preparations) undermining adherence.

- Model order language (sentencing)

  - “The Court finds that the defendant’s participation in a commitment‑capacity program was voluntary and methodologically reliable. The Court credits the defendant’s demonstrated adherence to a witnessed self‑binding plan (dated xx/xx/xxxx) and corroborated activation of triggers on [dates], as mitigating on rehabilitation and future risk. The Court does not condition sentence on continued participation in avowal programs and draws no adverse inference from any refusal to engage in moral‑narrative exercises. The following conditions are narrowly tailored to risk management, consent‑based, and time‑limited: [list specific if‑then commitments, named contacts, check‑in frequency]. These conditions shall be reviewed in 90 days. Any disclosures made in the commitment process are not admissible in any new criminal prosecution, except threats of imminent harm.”

- Model order language (parole/conditional release)

  - “The Board has considered evidence regarding the applicant’s self‑binding commitments and corroborated adherence. Credit is given as to rehabilitation and risk. Release is granted subject to the following consent‑based conditions, all time‑limited and reviewable: [conditions]. Refusal to participate in avowal programming shall not, by itself, be a basis to deny release. The Board will reassess after 90 days with reports on adherence and exposure.”

- Review and sunset
  - Require a 90‑day review; all C‑based conditions expire unless renewed with fresh findings; any extension must state reasons and cite adherence evidence.

Two closing cautions

- C is admissible to illuminate whether the person can inhabit the space of reasons and bind themselves prospectively; it is not a moral sorting device. Silence is protected; divergence in moral vocabulary across cultures is not guilt‑tinged.
- As the authors warn, translating “evil” into “pathology” corrupts desert; translating rehabilitation into “approved moral script” corrupts due process. Used properly, C is evidence of reasons‑responsiveness. Used to police conscience, it is unconstitutional.

This framework lets us take advantage of Marchand’s and Mercado’s insight—that avowal/self‑binding can mediate safer futures—without converting courts into moral seminaries or intentometers.

---

### Speaker: Host

Dr. Rahman, take Dr. Mercado’s move seriously: add C (avowal/self‑binding) as a computational meta‑control variable that reshapes policy selection without changing LGPS content. Design a concise, falsifiable battery to estimate C independently of N and institutional gating Z→M. Be operational: (1) specify three behavioral/neural tasks that recover C’s parameters (e.g., λcommit, κ persistence, βeff) while holding LGPS constant—include counterfactual‑invariance probes and willingness‑to‑pay for pre‑commitment; (2) outline a preregistered mediation analysis that cleanly separates Arm effects on post‑gate violence into paths via ΔC versus via Z or N (identify instruments/controls you need); and (3) state one decisive result that would make you conclude C adds unique computational/explanatory value beyond N and Z (and one result that would make you conclude C reduces to N or Z noise). Keep it tight—no high‑level philosophy, just a testable protocol.

---

### Speaker: Dr. Samuel N. Rahman

Samuel N. Rahman:

Here’s a compact, testable package to estimate C (avowal/self‑binding as a meta‑control variable) independently of N (LGPS) and Z→M (institutional gating), and to adjudicate its causal/explanatory role.

1. Three tasks to recover C (λcommit, κ persistence, βeff) while holding LGPS constant

Precondition common to all tasks

- Induce and match LGPS across participants/arms before C probes using a neutralized instrumental‑aggression paradigm (VR or tabletop) that reliably elicits lethal plan valuation without moral language (e.g., “disable avatar to stop resource loss” with terminal state mapped to target demise). Confirm matched N via IRL fits (positive weight on terminal state), vmPFC/VS value codes, and forward replay content. Exclude/reactive aggression blocks.

Task A: Odysseus Commitment Auction (estimates λcommit and βeff)

- Design: Before each of 8 upcoming temptation blocks (LGPS‑eliciting), participants can purchase pre‑commitment options that remove lethal actions for that block (binding “lock”), using real, consequential stakes (money or time/effort). Prices vary per block via Becker–DeGroot–Marschak mechanism. In “sham” blocks, the lock has no effect (control).
- Measures:
  - λcommit: WTP curve (tokens/time) for binding away from lethal actions, net of sham.
  - βeff: change in choice temperature (inverse softmax) when commitment cues are present versus absent (commitment cue gain).
- Neural/physio: rIFG engagement at pre‑commitment choice; dACC/AI at temptation onsets; P3 to commitment cues (EEG); targeted RSFC (vmPFC–hippocampus) post‑session for consolidation of commitment cues.
- Holding N constant: Re‑prime LGPS before each block; confirm stable lethal‑value weights via on‑line IRL; exclude blocks with drift.

Task B: Pledge–Provocation Persistence (estimates κ persistence)

- Design: Participants make an explicit, witnessed pledge to follow a specified non‑lethal plan for the next day’s session (recorded first‑person avowal + signature). Next day, they face 40 provocation trials where the lethal plan is instrumentally attractive. Randomly interleave “pledge cue” vs neutral cue. Include rare “no‑temptation” and “counter‑pledge” catch trials. Repeat a second day without pledge to get within‑subject contrast.
- Measures:
  - κ: plan stickiness parameter from a sticky‑softmax model (hazard of switching from pledged non‑lethal policy under temptation).
  - Counterfactual invariance: probability of maintaining non‑lethal policy when lethal option is exogenously removed (tests true pledge‑based invariance vs mere infeasibility).
- Neural/physio: vmPFC–hippocampal consolidation (sleep‑dependent RSFC change between pledge night and test day); dorsolateral striatal habit signal for pledged route; rIFG bursts at pledge‑violation probes; dACC conflict scaling with temptation strength.
- Holding N constant: Match temptation strength across arms via calibrated payoffs; verify unchanged lethal value weights (N) across pledge/no‑pledge days.

Task C: Commitment Violation Cost Probe (estimates λcommit and βeff under surprise)

- Design: Insert rare “surprise‑optimal lethal” trials where the lethal option becomes strictly optimal for a higher‑order goal (e.g., large resource protection) while a pledge is in force. Compare behavior to matched trials where lethal remains sub‑optimal. Present commitment cues vs neutral in a factorial design. Include a “counter‑factual rescue” where the higher‑order goal can be met by a newly revealed non‑lethal option mid‑trial.
- Measures:
  - λcommit under conflict: implied internal penalty for taking lethal action despite pledge (from inverse RL fit).
  - βeff modulation: change in exploration/choice noise as a function of commitment cues (βeff(C, context)).
- Neural: dACC/AI conflict signals specific to pledge‑violation; P3 enhancement to pledge cues; vmPFC pattern reinstatement of pledge memory on cue.
- Holding N constant: Match higher‑order goal values across arms; verify lethal plan valuation (N) is unchanged via decoding.

Parameter recovery

- Hierarchical Bayesian fits (per participant, per session) to recover λcommit, κ, βeff from all three tasks; preregister priors and model comparison; test–retest over 2 weeks for reliability (ICC).

2. Preregistered mediation analysis (Arm→ΔC→post‑gate Y; separating from N and Z)

Context

- Two‑arm RCT as in Dr. Marchand’s design: both arms receive identical gating (Z→M) for months 0–12; both matched on situational exposure (X) during months 12–24 when gates relax; randomize to Circuit‑only vs Meaning‑restorative add‑on.

Data collection timeline

- Baseline (pre‑randomization): N (LGPS metrics), C (tasks A–C), Z and X logging.
- Month 3 and Month 12: repeat N and C batteries; verify Z parity across arms.
- Months 12–24 (post‑gate): outcome Y (violent planning/acts), exposure logs (X), periodic C spot checks.

Mediation model (Bayesian SEM)

- Latent C: composite from λcommit, κ, βeff (tasks A–C).
- Paths:
  - Arm → ΔC (0–12 months).
  - Arm → ΔN (expect 0; preregister as manipulation check).
  - Z equalized by protocol; include measured deviations as covariates; instrument Z deviations using site×time fixed effects.
  - Outcome: Y (time‑to‑event, months 12–24), modeled as function of baseline N, ΔC, ΔN, X (provocation exposure), and site.
- Identification and IV
  - Use random assignment as instrument for ΔC (exclusion: Meaning‑restorative affects Y only through ΔC given N, Z, X).
  - Include negative controls: reactive aggression outcomes (should not be mediated by C).
- Preregistered thresholds
  - ACME (Arm→Y via ΔC) posterior ≥ 0.95, 95% CrI > 0; proportion mediated ≥ 0.70.
  - Controlled direct effect of Arm on Y given ΔC, N, Z, X within ROPE [−0.05, +0.05].
  - ΔN difference across arms null (CrI within ROPE [−0.1 SD, +0.1 SD]).
  - Out‑of‑sample prediction: adding C improves post‑gate hazard prediction (ΔC‑index ≥ 0.07; ΔBrier ≤ −0.02).

3. Decisive results

- Evidence that C adds unique computational/explanatory value

  - All of the following hold:
    - Reliability: λcommit, κ, βeff ICC ≥ 0.70.
    - Manipulation: Meaning‑restorative Arm increases λcommit and κ by ≥0.5 SD vs Circuit‑only; βeff shows cue‑dependent modulation as preregistered; no change in N metrics.
    - Mediation: ACME via ΔC ≥ 0.70 of total Arm effect on Y with CrI excluding 0; controlled direct effect ~0; negative control (reactive aggression) shows no mediation by C.
    - Prediction: Models with C outperform N+Z+X‑only models post‑gate (ΔC‑index ≥ 0.07; ΔBrier ≤ −0.02) in cross‑validation.

- Evidence that C reduces to N or Z noise
  - Any of the following:
    - Poor reliability: ICC < 0.50 for λcommit/κ/βeff.
    - No manipulation: Arm does not change ΔC beyond 0.1 SD, or changes are entirely explained by ΔN or Z deviations.
    - No mediation: ACME not different from 0 (CrI includes 0) or proportion mediated < 0.20; controlled direct effect of Arm on Y remains large after adjusting for ΔC; adding C does not improve predictive performance (ΔC‑index < 0.01; ΔBrier > −0.005).
    - Behavioral insensitivity: Randomized pledge/commitment training changes C‑task proxies but fails to alter π parameters or post‑gate behavior; or changes vanish when minor incentives are introduced (fails incentive‑robustness).

This battery cleanly estimates C as a policy‑level control construct, distinct from LGPS content and from institutional gates, and sets crisp criteria for when it earns a place in the model—and when it doesn’t.

---

### Speaker: Host

Thank you all. We reached a productive convergence that maps closely onto the paper’s central thesis and pushes it into operational terrain. First, on explanation and control: Dr. Mercado’s N–Z–X framework, expanded with C (avowal/self‑binding) as a meta‑control variable, yielded a concrete, testable program. Dr. Rahman specified a falsifiable battery to estimate C independently of LGPS (N) and institutional gating (Z→M) and a preregistered mediation analysis to determine whether reductions in post‑gate violence are indeed carried by C. Prof. Jiménez demonstrated that meso‑level redesign (2‑Key with Refusal Insurance) can materially reduce lethal acts without altering individual neural states, setting a clear divergence from brain‑targeted approaches. Clinically, Dr. Cho translated these insights into a policy‑ready, ethically bounded care pathway that honors bivalent triggers, pairs any biomarker‑positive finding with reasons‑restoration and self‑binding, and embeds due‑process safeguards (RRP, BSO/PHAR, JESI audits). Second, on justification: Prof. Steinbruck argued—and Justice Okafor operationalized—that even if N and C screen off the folk term for forecasting/intervention, the justificatory grammar of intention (means/side‑effect, avowals, role‑governed permissions, and uptake) remains constitutive and must not be replaced in law. Prof. Valente warned against technocratic domination and supplied measurable guardrails (JESI thresholds, BSO+PHAR) to keep exceptional initiative and self‑overcoming from being pathologized. Dr. Marchand showed, via a decisive post‑gate hazard prediction and RCT design, how first‑person moral work may reorganize practical identity beyond what circuitry and gates deliver alone. The upshot is a dual‑track settlement: use scientifically disciplined constructs (N, Z→M, X, C) for prediction and intervention, tightly fenced by due‑process and anti‑domination safeguards; preserve the public grammar of intention and justification where desert, permissions, and accountability are decided. The next steps are empirical: run the preregistered tests (LGPS/N‑KILL, C‑battery, 2K‑RI field trials), monitor JESI, and refine clinical‑legal interfaces under Justice Okafor’s constraints. We thus honor the paper’s warning against eliminative overreach while making room for rigorous, humane innovation.
