---
title: "The Hard Problem: Organization, Information, and Consciousness - Transcript"
date: "2025-09-12"
prev: 
  text: See write up
  link: '/The Hard Problem: Organization, Information, and Consciousness/summary.md'
next: false
---

### Speaker: Host

To kick us off: what would count as an empirical falsifier of your organizational invariance claim? Please name a concrete, operationalizable test (e.g., a cross‑substrate replication or neuromodulatory manipulation) that, if it produced a specific pattern of dissociation, would force you to abandon invariance. Frame it so Dr. Qureshi could imagine running it, and be precise about what must be matched as the “same fine‑grained organization.”

---

### Speaker: Prof. Gabriel Stone

Thanks—that’s exactly the right pressure point. If organizational invariance is more than an armchair slogan, there ought to be a way, in principle, to put it on the block. Here’s a concrete protocol I would happily live or die by.

What must be matched: “same fine‑grained organization”

By that I mean equivalence, up to a prespecified epsilon, of the causal structure and dynamics that matter for global availability and control. Operationally:

- Node-level dynamics: For each unit (neuron or prosthetic element), the conditional state-transition function P(s_t+Δ | inputs, state-history h≤T, modulatory inputs m) must be matched within epsilon across all inputs in a defined operating set U and over relevant time windows. This includes history dependence (e.g., refractoriness), stochasticity/noise statistics, and subthreshold integration.
- Edge-level structure: The directed connectivity, synaptic efficacies, delays, and short-term plasticity kernels must be matched; the effective connectivity matrix under perturbation (e.g., causal influence as measured by time‑resolved transfer entropy/Granger) must be indistinguishable.
- Learning/plasticity operator: Given the same input/history/modulatory conditions, the update rule for weights and intrinsic excitability (STDP/BTSP/metaplasticity) must be the same mapping within epsilon.
- Neuromodulatory sensitivity: Gain control and plasticity shifts under ACh, NA, DA, 5‑HT, etc., must preserve the same parameterized response surface; i.e., identical dose‑response curves and context dependence.
- Representational geometry and ignition: The representational similarity structure (RSA) in the local patch and downstream fronto‑parietal targets, and the conditions for recurrent “ignition,” must match across a battery of perturbations. Same attractor landscape (fixed points/limit cycles), same phase response curves, same cross‑frequency coupling profiles.
- Global access signature: The probability that information in the patch is broadcast and used for flexible task control (as indexed by meta‑d’, P3b/late positivity when report is required, fronto‑parietal recurrence when it isn’t, PCI/LZ under TMS) must be the same.

An empirical falsifier: closed‑loop microcircuit replacement with ABAB switching

Target
- A circumscribed visual color patch (e.g., ventral occipital V4/V8 columnar ensemble spanning a localized visual field region), where we can leverage rich psychophysics on hue, saturation, and brightness and where qualitative structure is well constrained.

Setup
1) Pre‑implant mapping. With laminar probes and microstimulation in surgical candidates (e.g., epilepsy), build a causal emulator of the target patch:
- Exhaustively probe the input–output map with temporally structured stimuli (naturalistic and noise) and optogenetic perturbations.
- Fit a neuromorphic “shadow circuit” (FPGA/analog VLSI) that reproduces node‑ and edge‑level dynamics, noise, plasticity, and neuromodulatory response surfaces under closed loop. Validate by interventional matching: for thousands of randomized perturbation patterns, the biological and shadow circuits produce indistinguishable downstream effects (same TE/Granger matrices, RSA, ignition probability).

2) Switchable replacement. Implant bidirectional interfaces that allow instantaneous routing of the biological afferents/efferents either through the native microcircuit or through the shadow circuit. Ensure that the “downstream” rest of cortex receives statistically indistinguishable signals under both routes across tasks and rest.

3) ABAB protocol. Run many short blocks with covert switching (A=biological, B=neuromorphic), counterbalanced and randomized, including:
- No‑report paradigms (e.g., binocular rivalry with eye‑movement and pupilometry inference, steady‑state responses).
- Report paradigms: fine‑grained hue/saturation matching, just‑noticeable‑difference thresholds, similarity‑space reconstruction, subjective intensity scales, and metacognitive confidence (meta‑d’), all localized to the replaced visual field patch vs. an adjacent control patch.
- Global measures: PCI via single‑pulse TMS outside the patch, LZ complexity, ignition probability for conscious access tasks, fronto‑parietal recurrence.

Predictions and falsifier
- Organizational invariance predicts: once the emulator passes the interventional matching battery, subjective color experience for stimuli confined to the replaced patch will be qualitatively indistinguishable from baseline. Psychophysical functions (e.g., the recovered 3D color space geometry), phenomenological reports (“the patch feels the same”), and metacognitive access will be unchanged, within the same epsilon tolerated in the causal matching.
- Falsifier: If, despite meeting all organizational equivalence criteria above (including interventional causal matching and modulatory sensitivity), the participant reliably reports a change in phenomenal character tied to the replaced patch—a stable shift in hue qualia (e.g., reddish feels greenish), a systematic desaturation, or an altered similarity geometry—while:
  a) task performance, reaction times, and metacognitive sensitivity are unchanged,
  b) representational geometry in the patch and downstream, ignition probability, PCI/LZ, and global workspace signatures are matched to baseline, and
  c) the effect is ABAB‑contingent (on when the switch is thrown), reproducible across days, and not eliminable by further tightening the causal‑matching tolerance,
then I would treat that as decisive evidence against organizational invariance. In plain terms: same causal organization, different qualia.

Two auxiliary, lower‑invasiveness falsifiers Dr. Qureshi could run sooner

1) Neuromodulatory isomorphism test (pain/affect).
- Use chemogenetic or pharmacological manipulations to replace native receptor families in a small insular/anterior cingulate patch with engineered receptors that implement indistinguishable gain/plasticity response surfaces (validated with in vivo opto/perturb‑and‑measure).
- If nociceptive discriminations, reflexes, and global access metrics remain matched, but the felt unpleasantness/intensity function shifts (e.g., pain “hurts less” at equal intensity across ABAB blocks), invariance is challenged.

2) Matched‑organization anesthesia dissociation.
- Titrate propofol and subanesthetic ketamine to match a rich set of organizational measures (PCI, LZ, effective connectivity, ignition probability, representational geometry in sensory cortex) at rest and during passive stimulation.
- If subjects later give convergent, time‑locked dream reports under ketamine but null reports under propofol, with organization measures matched to your tolerance, and if tightening the matching window fails to eliminate the dissociation, that’s evidence that substrate/biophysics matter beyond organization.

Why I accept these as falsifiers

- The invariance thesis is a modal claim: qualitative sameness supervenes on organizational sameness. I’ve operationalized “organizational sameness” by interventional causal equivalence, including plasticity and modulatory context. If we get the ABAB phenomenology without any organizational slippage detectable by very demanding causal probes, the most straightforward inference is that some non‑organizational property (substrate, biophysics) is doing constitutive work for experience—precisely Petrov’s view.
- I can’t, consistent with my own structural‑coherence constraint, demand that experience differ while every access signature is literally identical. So I’ve required that the difference in experience shows up only in first‑person reports localized to the manipulated content while the global signatures of access/integration remain matched. That is the tightest feasible empirical wedge.

Anticipating pushback

- Ellison will say any report difference just is a functional difference. That’s why the bar above includes exhaustive interventional matching and the requirement that global access indices, representational geometry, and metacognition remain constant. If after all that the only thing that moves is the way the color feels, I’m prepared to count that against invariance rather than move the goalposts indefinitely.
- Petrov will say we’ll never match “the right” biology. Fair: this is technologically extreme. But it is an honest target. If repeated attempts to close the organizational gap still yield substrate‑locked phenomenological shifts, that’s excellent evidence for biological essentialism.
- Tran may worry the organizational basis needs an information‑integration constraint. We’ve effectively built that in via ignition/PCI/causal‑density matching and RSA inferences; if adding her preferred integration metric as a matching criterion removes the dissociation, that’s friendly to my view.

Bottom line for Dr. Qureshi

- The V4/V8 ABAB microcircuit replacement is the cleanest falsifier. Short of that, the neuromodulatory isomorphism test and matched‑organization anesthesia dissociation are feasible near‑term approximations: if they produce substrate‑dependent phenomenology with matched organizational profiles, I will take that as serious, possibly fatal, evidence against organizational invariance. If they don’t, they strengthen the case that organization—not wetware per se—is what experience supervenes on.

---

### Speaker: Host

Stone’s ABAB microcircuit replacement posits “same causal organization, different qualia.” From your illusionist stance, do you (i) accept this as a genuine in‑principle falsifier, or (ii) insist that any reliable ABAB report of a phenomenal change logically entails a functional mismatch that his matching battery failed to capture? If (ii), name one concrete functional signature that must diverge whenever reports of 
“the color feels different” do—e.g., a shift in predictive error dynamics, metacognitive calibration (meta‑d’ vs d’), postdictive temporal integration windows, or priors over hue categories—and specify how Dr. Qureshi should instrument the ABAB design to detect it. Please be explicit: what metric, what threshold, and why would it inevitably move if the reports move?

---

### Speaker: Dr. Mira Ellison

(ii). If a participant can reliably ABAB‑discriminate “it feels different” while everything else is “matched,” that is already a functional fact about how evidence is being processed and read out. On my view, there is no room for a further phenomenal variable to flip independently of the generative/decision machinery. So I will name a specific signature that must move if the reports move, and show Qureshi how to catch it.

Concrete functional signature that must diverge: the postdictive temporal integration kernel for color appearance K(t)

Rationale
- In a predictive‑processing/multiple‑drafts architecture, “what it looks like now” is the current posterior over hue constructed by temporally pooling and precision‑weighting recent chromatic evidence and priors. If the subject can tell A vs B solely by “how the color feels,” some element of that pooling/weighting has changed. That shows up as a change in the temporal integration kernel that maps recent inputs to the posterior—i.e., the width/centroid/shape of K(t)—and in the associated precision‑weighted prediction‑error dynamics.
- Keeping representational geometry for static stimuli and ignition/PCI “matched” doesn’t guarantee K(t) is matched; postdiction is a bona fide degree of freedom. A phenomenological shift without any change in K(t) would mean the same stimulus time series is mapped to the same posterior at decision time, contradicting the fact that the person can tell the conditions apart.

How to instrument in the ABAB design

Stimuli and task
- High‑rate chromatic noise: Present 200–300 ms sequences at 120 Hz of small, independent steps in DKL color space around a reference hue for the retinotopic location confined to the replaced patch. Interleave with static probes already used by Stone so you can cross‑check geometry.
- Reverse‑correlation appearance report: On each trial, have the participant set a continuous pointer on a color wheel to “what it looked like” at the go cue. Collect confidence. No‑report blocks with eye‑tracking/pupilometry to infer moment‑by‑moment appearance can be added for triangulation.

Primary metric
- Psychophysical temporal kernel K(t): Estimate via ridge/logistic reverse correlation from the stimulus sequence s(t) to the reported hue angle at the cue. Fit a parametric causal kernel (e.g., difference of gammas) and extract:
  - Centroid (μ) of K(t) in ms.
  - Width (σ) or FWHM in ms.
  - Late/early weight ratio (area 120–250 ms vs 0–120 ms).

Confirmatory neural/physio signatures of precision‑weighting
- vMMN for chromatic oddball embedded in the same stream: MEG/ECoG/EEG deviance response amplitude and latency (reflecting prediction‑error updates).
- Spectral precision proxy: V4 gamma/beta power ratio during the window contributing to K(t); pupil dilation and microsaccade inhibition to deviants as a noradrenergic precision readout.

Thresholds and decision rule (pre‑register)
- Kernel difference: Declare a functional mismatch if any of the following exceed both (a) 15% of the condition‑wise mean and (b) 2 SD of test–retest variability within A blocks:
  - |μA − μB| > 12 ms
  - |σA − σB|/σpooled > 0.15
  - Late/early weight ratio difference > 0.15
  Use a hierarchical model to compare K(t) across ABAB with Bayes factor > 10 for a difference in any parameter as the confirmatory criterion.
- vMMN/precision checks (secondary): vMMN peak latency shift > 10 ms or amplitude change > 1.5 μV (EEG) and/or log gamma/beta ratio change > 0.2 during the kernel’s peak window; pupil deviant response change > 0.03 mm. These should covary with the K(t) shift.

Why this must move if the reports move
- A reliable ABAB report—“the same physical stimulus looks more/less saturated,” “the blend happens earlier/later,” “the hue feels slightly different”—is a difference in the mapping from the recent stimulus history to the judged appearance. In any Bayes‑like observer, that mapping is encoded in K(t) (and its precision weighting). Absent a change in K(t), the posterior at the report time is unchanged for any input sequence; you cannot get a systematic, switch‑contingent change in appearance without changing the temporal pooling that constructs it. That is, the very capacity to notice and report a difference entails a difference in the temporal integration/precision parameters.

Practical notes for Dr. Qureshi
- Fold the K(t) block into Stone’s ABAB switch with the same covert randomization. Keep performance matched by titrating stimulus range around the JND, so you don’t conflate kernel shifts with sensitivity changes.
- Fit a joint model that links the psychophysical K(t), vMMN dynamics, and confidence mapping (meta‑d’/d’). If reports differ but K(t) and precision proxies do not (within the thresholds above), I would attribute the ABAB reports to demand/expectancy or unmeasured slippage and ask to tighten instrumentation. If reports differ and K(t) (and ideally vMMN/precision) move in lockstep, that is exactly the functional difference my view predicts.

Bottom line
- I don’t accept “same organization, different qualia.” If you get ABAB phenomenology, you will find a functional wedge. The most diagnostic wedge here is the postdictive temporal integration kernel for color (and its precision‑weighted PE correlates). If you pre‑register the kernel metrics and thresholds above and the reports move while K(t) does not, I’ll eat my illusionist hat—but I predict you won’t get that dissociation.

---

### Speaker: Host

Jonas, put your biological naturalism on the line. Name one concrete, biologically specific causal feature you think is constitutive for consciousness that Stone’s organizational matching and Ellison’s K(t) kernel would still miss. Then design a targeted ABAB switch around that feature—keeping all of Stone’s organizational criteria and Ellison’s temporal‑integration metrics matched—to test your claim. Be precise: (i) what mechanism (e.g., active dendritic electrogenesis in layer‑5 pyramidal apical tufts; astrocytic Ca2+ tripartite signaling; specific neuromodulatory microdomain chemistry); (ii) how Dr. Qureshi instruments and replaces it (e.g., dynamic‑clamp channel replacement plus two‑photon Ca2+ imaging, local chemogenetic block with a neuromorphic proxy); (iii) what first‑person change you predict under B (e.g., reduced felt vividness/unity without performance loss); and (iv) what exact outcome would force you to soften substrate essentialism (e.g., no phenomenological change once dendritic NMDA/Ca2+ spike statistics are matched within X%). Keep it to a single mechanism and a falsifiable threshold so Amina could actually run it.

---

### Speaker: Prof. Jonas Petrov

Happy to put a crisp bet on the table.

Biology I claim is constitutive and missed by Stone/Ellison’s batteries
(i) Mechanism: active apical‑tuft calcium electrogenesis in layer‑5 pyramidal neurons (the Larkum/BAC‑firing motif). Specifically, regenerative NMDA/CaV‑dependent plateau spikes in distal tufts, gated by local HCN/M‑current and muscarinic ACh, that nonlinearly couple top‑down input in L1 to basal feedforward drive at the soma. My claim is not about “any old nonlinearity,” but about the living‑tissue microdomain: nanomolar–micromolar Ca2+ transients, submembrane diffusion/second‑messenger cascades (CaM/PKA/SK), and their time‑dependent effect on dendrite‑soma coupling. That biophysical event is part of what makes a content consciously felt.

Targeted ABAB switch keeping Stone and Ellison matched
(ii) Instrumentation/replacement (ventral occipital color patch; macaque is most realistic first, with a human‑patient variant below).

A. Verify/characterize the biological mechanism
- Expression: GCaMP in L2/3–L5 pyramidal neurons; red‑shifted inhibitory opsin targeted to apical tufts (e.g., soma‑sparing ArchT with dendritic targeting motif).
- Recording: laminar probes (L1–L6) for local/top‑down streams; multiarea readouts to FEF/LPFC/IPS; widefield + 2‑photon tuft Ca2+ imaging in the retinotopic V4/V8 patch representing a small visual field location used in Stone’s color task.
- Modulatory context: microdialysis for ACh/NE markers; cholinergic tone manipulations (local physostigmine/atropine) to map response surfaces.

B. ABAB manipulation and prosthetic proxy
- Switch A (intact): no shunt; record tuft Ca2+ plateaus and bAP–tuft coincidence.
- Switch B (biophysics suppressed, organization preserved): optically shunt apical tufts to suppress Ca2+ plateau electrogenesis (>80% reduction in plateau incidence/area by 2‑photon readout) while simultaneously running a closed‑loop apical‑proxy that restores all downstream causal organization:
  - Sense: laminar L1–L3 top‑down activity and basal drive in L4/L5 via probes.
  - Compute: in real time, a fitted dendrite‑soma transfer operator that predicted, on A‑blocks, the somatic contribution of tuft plateaus (history‑ and neuromodulator‑dependent).
  - Actuate: drive an excitatory optogenetic conductance at the apical trunk/soma (or dynamic‑clamp if feasible) to inject the predicted current so that somatic spike trains, burst statistics, and downstream effective connectivity match A.
- Matching to Stone’s criteria: pre‑register epsilons and validate that under B, relative to A:
  - Node‑level: spike‑train Victor–Purpura distance < 0.1; burst probability, ISI distributions, and refractory‑history effects within 5%; noise statistics matched.
  - Edge/effective connectivity: time‑resolved TE/Granger matrices within 5% RMSE; causal PRC/phase‑reset curves indistinguishable.
  - Plasticity operator: same STDP/BTSP update curves under the same perturbations (within 5%).
  - Neuromodulatory sensitivity: identical dose–response surfaces to local ACh/NE manipulations (fit parameter differences < 5%).
  - Representational geometry/ignition: RSA r > 0.95; ignition probability difference < 2%; PCI/LZ under TMS within 5%.
- Matching to Ellison’s K(t): embed her high‑rate chromatic noise and reverse‑correlation block; fit K(t) and require |Δμ| < 10 ms, |Δσ|/σpooled < 0.1, late/early ratio Δ < 0.1; vMMN latency/amplitude and gamma/beta precision proxies within her thresholds.

C. Human‑patient variant (if macaque is not on the table)
- No opsin/genetics: suppress L1 electrogenesis pharmacologically (very focal NMDA/L‑type antagonists via microcatheter) while using closed‑loop microstimulation at the apical trunk/soma to reproduce the A‑block somatic/burst statistics and downstream effective connectivity; validate with laminar recordings and Stone/Ellison matching as above. Use no‑report color paradigms and VAS ratings intraoperatively.

First‑person prediction under B (with all the above matched)
(iii) Predicted change: a selective reduction in phenomenal vividness/presence (“washed‑out,” “flatter,” less compelling) for color restricted to the replaced visual field patch, with:
- No change in identification/discrimination thresholds, RTs, meta‑d’/d’, RSA geometry, ignition, PCI/LZ, or Ellison’s K(t).
- Quantify with pre‑anchored continuous ratings:
  - Vividness/saturation VAS (0–100) anchored to physical calibrators.
  - “Compellingness” of color‑spread illusions (neon color spreading/watercolor) confined to the patch, rated independently of task choice.
- Effect size expectation: mean VAS drop ≥ 10–15 points (Cohen’s d ≥ 0.5) ABAB‑contingent, reproducible across days, dose‑dependent with degree of tuft plateau suppression, and uncoupled from K(t) and global access indices.

What would make me soften substrate essentialism
(iv) Falsifier/threshold: If, after confirming tuft‑plateau suppression ≥ 80% by 2‑photon Ca2+ (or best available proxy) and after meeting all Stone/Ellison matching tolerances above, the ABAB difference in vividness/compellingness is ≤ 3 VAS points (Cohen’s d < 0.2) with Bayes factor < 1/3 supporting no effect across ≥ 10 sessions (and illusions’ compellingness likewise unchanged), I will soften my substrate essentialism. Concretely: I would drop the claim that apical‑tuft calcium electrogenesis is constitutive, and concede that organization at the granularity we matched suffices, at least for this domain of color phenomenology.

Why this puts pressure where it should
- Stone’s invariance lives or dies on exhaustive causal matching. We give him that, including modulatory context and Ellison’s temporal integration. What we remove is a specific living‑tissue causal power: regenerative Ca2+ microdomain electrogenesis in apical tufts. If phenomenal vividness moves while organization (by his own lights) and K(t) are fixed, biology matters.
- If nothing moves, that’s evidence against my constitutivist hunch about this mechanism. I’m prepared to take that on the chin.

Ellison will say “a vividness report just is a functional change.” That’s exactly why I’ve pre‑registered the functional signatures she cares about (posterior construction via K(t), precision proxies, metacognitive calibration) and required they stay put. If a residual, content‑localized change in “how it feels” survives that clamp, you don’t get to explain it away by pointing to an unmeasured postdictive kernel; you’d need to show which kernel moved.

In short: apical‑tuft Ca2+ electrogenesis is my biological line in the sand; the ABAB design above gives Amina a way to erase it biophysically while holding fixed the causal organization Stone and Ellison demand. If phenomenal vividness is invariant under that erasure, I’ll revise. If it isn’t, they should.

---

### Speaker: Host

Feasibility triage: of the three proposals on the table (Stone’s V4/V8 ABAB microcircuit replacement, Ellison’s K(t) temporal‑integration assay, Petrov’s apical‑tuft Ca2+ ABAB), pick one you could realistically execute in the next 12–18 months in humans or perioperative patients. Please outline a pre‑registered protocol with (i) population and instrumentation (e.g., TMS‑EEG, high‑density EEG/MEG, intracranial ECoG/laminar when available), (ii) your operational “organizational matching” criteria and thresholds, incorporating at least PCI/LZ, ignition probability, RSA stability, and Ellison’s K(t) kernel, (iii) the phenomenology readout (reports or no‑report proxies) and the exact dissociation you would treat as evidence against organizational invariance (or for Petrov’s substrate claim), including numeric thresholds/Bayes factors, and (iv) one major confound you expect (e.g., arousal/neuromodulator drift, expectancy) and how you will guard against it (e.g., covert ABAB, pharmacokinetic modeling, blinding). Keep it to a single, executable study plan with concrete numbers so we can judge whether it would actually move the needle.

---

### Speaker: Dr. Amina Qureshi

Short answer: I can execute Ellison’s K(t) temporal‑integration assay in a within‑subject, double‑blind, cross‑over drug study that matches a rich organizational profile (PCI/LZ, ignition probability, RSA) and asks whether phenomenology diverges anyway. Stone’s implantable ABAB is not human‑feasible in 12–18 months; Petrov’s dendritic ABAB needs opsins or focal pharmacology we don’t have ethically in patients. The K(t) assay with tight organizational matching we can do now.

Pre‑registered protocol

(i) Population and instrumentation
- Cohort A (healthy volunteers): n=24, 20–45 yrs, normal color vision. Instrumentation: 256‑ch HD‑EEG (with eye‑tracking/pupilometry), TMS‑EEG for PCIst, psychophysics. Subsample (n≈12) add whole‑head MEG for source‑space RSA.
- Cohort B (epilepsy perioperative/monitoring): n=6–8 with occipito‑temporal ECoG (preferably covering V4/V8) and some fronto‑parietal coverage. Intracranial stimulation constraints observed. Optional single‑pulse TMS in non‑implanted hemisphere for PCIst if safe; otherwise PCI proxy via perturbational LZ under single‑pulse electrical stimulation.
- Drugs: Double‑blind, randomized, cross‑over sessions (AB/BA; ≥7 days apart):
  - Low‑dose propofol (target‑controlled infusion).
  - Subanesthetic S‑ketamine (0.3–0.5 mg/kg/hr with bolus as needed).
  Closed‑loop titration to an organizational target (see ii). Continuous cardiorespiratory monitoring; arterial line in Cohort B (and in a subset of Cohort A if approved) to measure plasma levels.

(ii) Organizational matching: metrics and thresholds
We pre‑register an “organization window” and only analyze epochs that meet all criteria simultaneously.

- Global complexity/perturbation
  - PCIst (TMS‑EEG): |ΔPCIst| ≤ 0.05 absolute units (normalized 0–1) between drugs at matched target; session‑wise SD ≤ 0.03.
  - Resting LZ (HD‑EEG, 2–45 Hz, 60‑s windows): |ΔLZnorm| ≤ 0.05.

- Ignition probability (visual near‑threshold task; backward masking and RSVP oddball)
  - Define ignition as late (>300 ms) fronto‑parietal positivity (P3b‑like) plus a rise in directed connectivity (time‑resolved transfer entropy) from occipital to FPN.
  - Match the probability of ignition across 500 trials: |ΔP(ignition)| ≤ 0.03. Also match d′ within 0.1 and RT within 30 ms.

- Representational stability (RSA) for color
  - Source‑localized (MEG/EEG) or ECoG multivariate patterns for a 36‑hue DKL grid. Correlate representational dissimilarity matrices (RDMs): Spearman r ≥ 0.90 across drugs; bootstrapped 95% CI lower bound ≥ 0.85. In ECoG (Cohort B), require r ≥ 0.95 in contacts mapping the retinotopic patch.

- Temporal integration kernel K(t) (Ellison)
  - High‑rate chromatic noise (120 Hz) reverse‑correlation to estimate K(t) parameters. Matching thresholds: |μA−μB| ≤ 10 ms; |σA−σB|/σpooled ≤ 0.10; late/early area ratio Δ ≤ 0.10. vMMN latency shift ≤ 10 ms; amplitude Δ ≤ 1.5 μV; log gamma/beta ratio Δ ≤ 0.2; pupil deviant response Δ ≤ 0.03 mm.

We implement closed‑loop drug titration to hit these targets (adaptive adjustments every 2–3 min based on running estimates of PCI proxy, LZ, and ignition probability), and we pre‑register a composite “match index.” Sessions failing the match are repeated; trials outside the window are excluded a priori.

(iii) Phenomenology readouts and dissociation criterion
Tasks are restricted to the retinotopic location used for RSA to localize content.

- Real‑time phenomenology (during matched windows)
  - Color vividness/saturation VAS (0–100), anchored to physical calibrators (photometrically matched saturations).
  - Compellingness of color‑spread illusions (neon color spreading, watercolor) confined to target location (VAS).
  - “Naturalness”/“presence” ratings for briefly presented natural images tinted with target hues (to avoid pure demand).
  - Confidence ratings for color appearance (for meta‑d′). We keep d′ and meta‑d′ matched (Δ ≤ 0.1) by staircase if needed.

- No‑report adjuncts
  - Binocular rivalry pupil/OKN signature strength for chromatic gratings; switch rate distributions.
  - Spontaneous imagery probes (thought‑sampling beeps with button press for “currently seeing colors with eyes closed?” in eyes‑closed blocks).

- Post‑hoc experience
  - Structured micro‑phenomenology interview immediately post‑block for drug‑paired differences (color richness, presence of dream‑like imagery). Pre‑register core items (11D‑ASC color/visual subscales).

Evidence against organizational invariance (and consistent with Petrov’s substrate sensitivity) will be declared if, within matched organizational windows:
- Primary criterion: Mean VAS vividness or illusion compellingness differs by ≥10 points (Cohen’s d ≥ 0.5) between drugs, replicated within participant across two sessions, with a group‑level Bayes factor BF10 ≥ 10 (Bayesian hierarchical model) and frequentist p < 0.01 (Bonferroni‑corrected).
- And K(t) parameters meet match thresholds (all three; Bayes factor for equivalence BF01 ≥ 3).
- And RSA r, ignition probability, PCIst, LZ remain within thresholds above (session‑wise checks; BF01 ≥ 3 for equivalence on each).
- Secondary: Dream/imagery report probability differs by ≥25% (BF10 ≥ 10) during eyes‑closed matched windows, with no change in global organization metrics.

Conversely, if phenomenology does not differ (BF01 ≥ 3 for no difference) once K(t) and organizational metrics are matched, that supports an invariance‑friendly picture (at least that our operational “organization” is sufficient for these contents in these states).

Power
- With n=24 within‑subject and expected d≈0.5, 1−β > 0.8 at α=0.01. We anticipate 15–20% data loss from unmatched windows; we’ll oversample to n=28 if needed. Cohort B is exploratory/confirmatory of RSA/ignition details.

(iv) Major confound and mitigation
- Confound: Arousal/neuromodulator drift and expectancy.
  - Mitigation:
    - Double‑blind, double‑dummy infusion (both pumps running each session; only one active). Randomized order; identical room setup, music off, eyes‑open/closed blocks fixed.
    - Pharmacokinetic/pharmacodynamic modeling with plasma sampling (Cohort B; subset of Cohort A) to ensure comparable exposure.
    - Closed‑loop control to hold the organizational indices at target; discard epochs where indices stray.
    - Masked task framing; deception check post‑hoc to assess drug‑guessing. Exclude sessions where correct guesses > chance with high confidence.
    - Pre‑registration, independent data‑monitoring to prevent p‑hacking; analysis scripts frozen.

Why this would move the needle
- It’s the cleanest human‑feasible way to ask: when you really do hold the usual “organization” suspects fixed (perturbational complexity, ignition, representational geometry, and postdictive K(t)), does phenomenology float? If yes, that pressures invariance (or shows our organizational surrogate set is still missing something biophysically specific, à la Petrov). If no, it strengthens the case that the functional/organizational story—at least at this granularity—does most of the explanatory work for conscious color appearance.

Caveat from my shop
- Whatever we find, I will treat it as a constraint, not a metaphysical verdict. A positive dissociation would tell me to look harder at state‑dependent biophysics (e.g., receptor‑level precision control) as part of the minimally sufficient neural mechanisms of awareness. A null would push me to tighten our organizational measures further before invoking new “extra ingredients.”

---

### Speaker: Host

Amina’s plan matches PCI/LZ, ignition probability, RSA, and Ellison’s K(t). From your double‑aspect information view, name one additional informational invariant that must be matched to legitimately claim “same organization”—ideally something capturing synergistic integration rather than just complexity. Please specify a concrete, implementable proxy (e.g., O‑information/PID‑based synergy across occipito‑parietal‑frontal triads or an IIT‑style Φ* surrogate), how to compute it with her EEG/MEG/ECoG setup, and exact thresholds you’d require (numeric deltas/equivalence bounds). Also, state your prediction for ketamine vs propofol under Amina’s protocol: which way should this invariant move, and how would a phenomenology difference with this invariant matched (vs mismatched) bear on organizational invariance and your double‑aspect constraints? Keep it to a single invariant, one pipeline, and clear numbers so she can pre‑register it.

---

### Speaker: Dr. Linh Tran

Great—if we’re going to claim “same organization” in a double‑aspect/information sense, we have to match not just complexity and access, but the specifically synergistic component of cross‑areal information integration. My one invariant:

Informational invariant to add: synergistic integrated information across occipito‑parietal‑frontal triads (ΦIDsyn)

- What: The synergistic portion of time‑lagged mutual information between the past and present of a meso‑scale triad {occipital color area, posterior parietal, lateral prefrontal}, estimated via the integrated information decomposition (PhiID). This isolates information about the triad’s future that is only available from the joint state of two or more nodes (true synergy), not from any node alone or redundantly. It is the most direct, implementable proxy for “integration” I’m willing to treat as constitutive, beyond PCI/LZ and ignition.
- Why: PCI/LZ index richness/compressibility, ignition indexes access/broadcast, RSA captures representational geometry, and K(t) captures postdictive pooling. None of these tell you whether the content depends on joint states in a way irreducible to parts. My bridge‑principles require that phenomenal unity/structure ride on such synergistic informational invariants in recurrent networks.

Single pipeline Dr. Qureshi can pre‑register

Signals/ROIs
- EEG/MEG: source‑reconstruct to cortex (beamformer/LCMV), parcellate with HCP‑MMP.
- ECoG: select electrodes covering ventral occipital color patch (V4/V8 homolog), IPS/SPL, and dlPFC/FEF.
- Define left/right triads: O=V4/V8 patch matching the psychophysics location; P=IPS1/2; F=area 8/46 or FEF. Pre‑register 8–12 triads (bilateral, plus a few control triads not spanning all three lobes).

Preprocessing
- Bandpass 2–45 Hz; downsample to 250–500 Hz; artifact removal; z‑score each channel within session.
- Gaussian‑copula transform each ROI time series (rank‑to‑normal) to use closed‑form Gaussian information estimators while being robust to non‑Gaussianity.

PhiID synergy computation (time‑lagged)
- For each triad X(t)=[xO(t), xP(t), xF(t)] and lag τ=10 ms (sensitivity check at 5, 20 ms):
  - Form joint vector [X(t−τ), X(t)] in 200–300 ms post‑stim windows (and matched resting windows).
  - Estimate covariance of the Gaussian‑copula variables; compute I(X(t−τ); X(t)) and decompose via PhiID into redundant, unique, and synergistic components using the Gaussian PID/PhiID closed‑forms.
  - Define ΦIDsyn (bits) and the synergy fraction s = ΦIDsyn / I(Xpast; Xpresent).
- Aggregate within participant: average ΦIDsyn and s across windows and trials, separately for task and rest, and across triads (report both triad‑wise and mean).

Equivalence bounds to claim “matched organization”
- Primary bound (fraction): |Δs| ≤ 0.03 absolute AND ≤ 10% of the across‑drug mean s, for the triad‑mean and for ≥ 80% of individual triads (per participant).
- Bits bound: |ΔΦIDsyn| ≤ 0.02 bits (triad‑mean), with test–retest reliability > 0.8 and between‑drug difference within 0.5 SD of within‑session variability.
- Distributional bound: two‑sample KS distance between triad‑wise s distributions ≤ 0.10.
- Equivalence statistics: TOST or Bayesian ROPE with BF01 ≥ 3 for equivalence on s and ΦIDsyn at both participant and group levels.

Computation details
- Windows: 100–300 ms post‑stim for appearance tasks; 60‑s sliding windows (step 10 s) for rest.
- Frequencies: primary analysis on broadband (2–45 Hz). Sensitivity analyses on alpha‑beta (8–25 Hz) and gamma (30–45 Hz) by applying the same pipeline to Hilbert amplitude envelopes (copula‑Gaussian again).
- Code: pre‑register a PhiID implementation (e.g., Mediano/Rosas phiID toolkit; Gaussian PID closed‑form) with unit tests on synthetic data to confirm synergy selectivity.

Prediction: ketamine vs propofol under Amina’s matched‑metrics protocol
- My bet: even when PCI/LZ, ignition, RSA, and K(t) are matched, ketamine will show higher ΦIDsyn and s across O‑P‑F triads than propofol (Δs ≈ +0.04 to +0.06; ΔΦIDsyn ≈ +0.02 to +0.04 bits), reflecting preserved/enhanced joint integration of internally generated/top‑down and sensory signals. Propofol tends to flatten cross‑areal synergy toward redundancy even when complexity is forced to match.
- Practical note: you may need to steer ketamine to a target where dissociative content is present but access metrics are matched; the synergy difference should persist unless you explicitly titrate it away.

How to interpret outcomes vis‑à‑vis invariance and my double‑aspect constraints
- Phenomenology differs and ΦIDsyn is mismatched: That’s the pattern I expect. It supports the claim that synergistic informational structure—not just complexity/broadcast/geometry/temporal pooling—is the right organizational axis for mapping to qualitative structure. It helps reconcile any ketamine–propofol phenomenology split with an organizational (not substrate) story.
- Phenomenology differs and ΦIDsyn is matched (within bounds above): That pressures my view. I would first extend the invariant to higher‑order synergy (k>3 sets; e.g., adding thalamus or anterior insula) or cross‑frequency synergy (phase–amplitude PhiID), but if repeated studies keep phenomenology diverging with triad‑ and 4‑node ΦIDsyn matched, I would take that as evidence that either (a) our operational “organization” still misses the relevant informational invariant, or (b) Petrov is right that microphysical specifics contribute constitutively. I would count (b) as live if we exhaust (a).
- Phenomenology does not differ once ΦIDsyn is also matched: That strengthens organizational invariance and is exactly the convergence I’d expect if our invariant is the right bridge variable.

Pre‑registerable numbers (for Amina)
- Triads: ≥ 10 per participant; τ=10 ms primary; windows 100–300 ms.
- Equivalence bounds: |Δs| ≤ 0.03 and ≤ 10%; |ΔΦIDsyn| ≤ 0.02 bits; KS ≤ 0.10; BF01 ≥ 3 for equivalence at participant and group levels.
- Expected ketamine–propofol offset (if unmatched): Δs ≈ 0.05; ΔΦIDsyn ≈ 0.03 bits.

Bottom line
- Add ΦIDsyn across O‑P‑F triads as a pre‑registered invariant. If we don’t control synergy, we haven’t really matched the informational organization that, on a double‑aspect view, should co‑vary with how the content is experienced.

---

### Speaker: Host

You’ve argued quantum dynamics could be the ‘extra ingredient.’ Give us one falsifiable, human‑feasible quantum‑specific invariant to add to Qureshi’s protocol that is not reducible to classical organizational metrics she’s matching (PCIst/LZ, ignition, RSA, K(t), and Tran’s ΦIDsyn). My suggestion to focus you: a nuclear‑spin test with xenon anesthesia. Can you pre‑register (i) the invariant (e.g., spin‑dependent decoherence/relaxation reflected in in‑vivo hyperpolarized 129Xe T1/T2* or a spin‑specific effect size on anesthetic potency), (ii) a double‑blind cross‑over design comparing 129Xe (I=1/2, nonzero spin), 131Xe (I=3/2), and 134Xe (I=0) at matched end‑tidal partial pressures while holding Qureshi’s organizational window and Tran’s ΦIDsyn within equivalence bounds, (iii) the phenomenology you predict will differ across isotopes (e.g., dream incidence/vividness or dissociative content at equal PCIst/ΦIDsyn), and (iv) numeric thresholds that would count for/against the quantum hypothesis (e.g., ≥15% shift in loss‑of‑responsiveness concentration or ≥10‑point VAS vividness difference between spinful vs spin‑zero xenon with |ΔPCIst|≤0.05, |ΔΦIDsyn|≤0.02 bits)? Also name one quantum‑level metric you’d require to move with phenomenology (e.g., isotope‑dependent 129Xe cortical T1 change ≥10% or terahertz Raman peak Q‑factor change), and how we’d measure it noninvasively. If these spin manipulations yield no phenomenology differences once the classical/ΦIDsyn metrics are matched (Bayes factor for equivalence ≥3), would you soften the quantum ‘extra ingredient’ claim for this domain?

---

### Speaker: Prof. Victor Hale

Thanks—this is exactly the sort of make‑or‑break test I’d like us to run. If quantum degrees of freedom really matter, we should be able to surface a nuclear‑spin–dependent signature that survives after Amina has clamped the entire classical/organizational profile and Linh’s synergy invariant. Xenon gives us a uniquely clean handle.

Pre‑registered quantum‑specific invariant

Invariant: nuclear‑spin–dependent anesthetic potency together with an in‑vivo cortical xenon spin‑relaxation signature

- Potency component (behavioral/physiological): a systematic shift in the end‑tidal concentration required to reach a fixed organizational target (the “LOR50”/organizational‑match dose) as a function of xenon isotope nuclear spin. Prediction: spin‑zero 134Xe (I=0) is more potent (lower LOR50) than spinful 129Xe (I=1/2), with 131Xe (I=3/2) the least potent of the three (i.e., 134Xe < 129Xe < 131Xe in organizationally matched dose), consistent with prior animal hints of spin effects.
- Spin‑relaxation component (MR): in‑vivo changes in the dissolved‑phase hyperpolarized 129Xe longitudinal and effective transverse relaxation (T1, T2*) and chemical‑shift spectra within cortex that track phenomenology across isotopes. This is quantum‑specific because the relaxation and spectral partitioning of the nuclear spin depend on hyperfine/quadrupolar couplings at putative anesthetic target sites; it is not reducible to PCI/LZ/ignition/RSA/K(t)/ΦIDsyn.

Design: double‑blind, triple cross‑over with isotope control and classical/ΦIDsyn clamping

Population/instrumentation
- Healthy volunteers: n=24; 256‑ch HD‑EEG, TMS‑EEG for PCIst, eye‑tracking/pupilometry; subset n=12 with MEG; all sessions in a xenon‑capable anesthesia suite.
- HP‑129Xe MR spectroscopy: dedicated xenon RF head coil at 1.5–3 T; dissolved‑phase spectroscopy focused on gray matter (occipito‑temporal ROIs) with interleaved gas/tissue reference peaks. We use brief tracer puffs of HP‑129Xe during each session (see below), safe and standard in lung MR; here, optimized for brain MRS.

Drug conditions (3 sessions, ≥7‑day washout; order randomized, triple‑blind)
- Session A: 129Xe‑enriched xenon (I=1/2).
- Session B: 131Xe‑enriched xenon (I=3/2).
- Session C: 134Xe‑enriched xenon (I=0).
End‑tidal monitoring with fast gas analyzers; matched O2, ETCO2, temperature, and hemodynamics.

Two regimes per session (pre‑registered)

1) Matched end‑tidal steps (dose–response)
- Stepwise end‑tidal plateaus (e.g., 20%, 30%, 40% Xe in O2/air) for 10–12 min each, identical across isotopes. We quantify classical metrics, ΦIDsyn, and phenomenology at each step. This yields raw potency curves and any “spin at equal dose” phenomenology differences.

2) Matched organization window (closed‑loop clamping)
- Closed‑loop titration of end‑tidal xenon to hit Amina’s equivalence bounds for:
  - PCIst: |Δ| ≤ 0.05
  - Resting LZnorm: |Δ| ≤ 0.05
  - Ignition prob.: |Δ| ≤ 0.03 (with d′, RT within Amina’s bounds)
  - RSA (color RDMs): r ≥ 0.90 (MEG/EEG), ≥ 0.95 (ECoG if available)
  - K(t): |Δμ| ≤ 10 ms; |Δσ|/σ ≤ 0.10; late/early Δ ≤ 0.10; vMMN/precision proxies within Ellison’s thresholds
  - ΦIDsyn (Tran): |Δs| ≤ 0.03 AND ≤10% of mean; |ΔΦIDsyn| ≤ 0.02 bits; KS ≤ 0.10; BF01 ≥ 3 for equivalence
We record the end‑tidal concentration required to maintain this window in each isotope session (the organizational‑match dose).

HP‑129Xe spin‑relaxation assay (quantum metric)
- In every session (including 134Xe and 131Xe runs), we deliver brief, low‑fraction “tracer” inhalations of hyperpolarized 129Xe during the window (e.g., two 10–15 s breaths separated by ≥3 min), superimposed on the background isotope. This does not materially alter sedation level but provides a readout of the local spin‑relaxation environment.
- We acquire dissolved‑phase cortical 129Xe spectra and estimate:
  - T1 (inversion‑recovery or saturation‑recovery) and T2* (line width) in cortex.
  - Chemical‑shift partitioning: relative amplitudes of tissue/blood peaks and any resolved down‑field components indicative of binding in hydrophobic cavities.
- For 131Xe (quadrupolar), we optionally retune to 131Xe and acquire exploratory spectra to estimate its (expected shorter) T1/T2*; feasibility‑contingent and not required for the primary analysis.

Phenomenology readouts (within the organization window)
- VAS ratings (0–100) for dreamlike imagery/vividness, dissociation, and chromatic vividness/“presence” for the color tasks (anchored to physical calibrators).
- Incidence of conscious mentation in eyes‑closed blocks (thought sampling), micro‑phenomenology focused on visual content/dream quality; no‑report proxies (rivalry OKN/pupil).
- Keep task performance and meta‑d′ matched via staircase so we isolate qualitative changes.

What I predict will differ across isotopes (with PCI/LZ/ignition/RSA/K(t)/ΦIDsyn matched)
- Organizational‑match dose (primary potency metric): 134Xe < 129Xe < 131Xe, with:
  - Δ(134 vs 129) ≥ 15% in end‑tidal concentration (LOR50 or organizational‑match dose).
  - Δ(129 vs 131) ≥ 7% (same direction).
- Phenomenology: at the clamped organization target, spinful isotopes will permit more residual conscious mentation/dreamlike content than spin‑zero 134Xe, reflected in:
  - VAS vividness/dissociation differences ≥ 10 points (Cohen’s d ≥ 0.5), ABAB‑consistent within subjects; BF10 ≥ 10 at group level.
  - Dream incidence difference ≥ 25% (ketamine‑style dissociation is not the goal here; we’re looking for imagery and “presence” at equal PCI/ΦIDsyn).
- Quantum metric co‑movement: cortical dissolved‑phase 129Xe T1/T2* changes will track phenomenology and potency across sessions:
  - T1 shortening under the more “consciousness‑suppressing” condition (typically 134Xe) by ≥ 10% relative to the more mentation‑permissive condition (typically 129Xe); or a systematic shift in the relative amplitude of down‑field tissue peaks by ≥ 15%, consistent with altered occupancy of hydrophobic binding pockets.
  - Across participants, |r| ≥ 0.4 between ΔT1 (or Δline width) and VAS vividness/dream incidence, controlling for classical metrics (partial correlation); BF10 ≥ 10.

Decision thresholds (pre‑registered)

Evidence for a quantum spin effect (supporting a quantum “extra ingredient” in this domain) if all of the following hold:
- Organizational‑match dose shows the predicted spin ordering with differences meeting or exceeding:
  - Δ(134 vs 129) ≥ 15% (95% CI excludes 0; BF10 ≥ 10).
  - Δ(129 vs 131) ≥ 7% (95% CI excludes 0; BF10 ≥ 10).
- Within the organization window (all classical metrics and ΦIDsyn in equivalence as above), phenomenology differs by:
  - ≥ 10 VAS points for vividness/dissociation (BF10 ≥ 10) and/or dream incidence Δ ≥ 25% (BF10 ≥ 10).
- Quantum metric moves with phenomenology:
  - ΔT1 (or ΔT2*) ≥ 10% between the “more suppressive” vs “more permissive” isotope sessions, and |r| ≥ 0.4 between ΔT1 and VAS vividness across subjects (BF10 ≥ 10).
Failing any of these, we do not count the result as positive.

Confounds and why this is quantum‑specific
- Classical explanations (solubility, diffusion, MAC differences unrelated to spin) are controlled by (a) clamping the classical organizational window, (b) matching ETCO2/O2/hemodynamics, (c) cross‑over, triple blinding, and (d) requiring the spin‑relaxation co‑movement. Nuclear spin (I) changes hyperfine/quadrupolar interactions and thus T1/T2*, which are not parameters in PCI/LZ/ignition/RSA/K(t)/ΦIDsyn. If the phenomenology and potency track I while those classical metrics are held fixed, the simplest explanation is that spin‑dependent quantum interactions are in play.

What would count against the quantum claim here?
- If, after meeting Amina’s and Linh’s equivalence bounds (PCIst/LZ/ignition/RSA/K(t)/ΦIDsyn all within pre‑registered limits), we find:
  - Organizational‑match doses do not differ across isotopes beyond ±5% (BF01 ≥ 3 for equivalence),
  - VAS/dream incidence do not differ (BF01 ≥ 3 for equivalence),
  - And the HP‑129Xe cortical T1/T2* (and spectral partitioning) show Δ < 5% with no correlation to phenomenology (BF01 ≥ 3 for equivalence),
then I will soften the quantum “extra ingredient” claim for the anesthesia/mentality domain specifically: I would conclude that nuclear‑spin–dependent radical‑pair–style interactions (or xenon‑spin coupling to putative quantum substrates) are unlikely to be doing constitutive work for conscious phenomenology under xenon in humans. I would not generalize this to all quantum proposals (e.g., objective‑reduction dynamics), but it would remove one of the most testable quantum footholds.

Why this matters in the broader debate
- Gabriel’s organizational invariance gets a fair shake: we obey his most stringent matching plus Linh’s synergy. If qualia still shift with I while organization (including ΦIDsyn) does not, that’s a direct hit on pure organizational sufficiency.
- Mira will insist any report difference implies a functional leak. That’s why we’ve pre‑registered not only her K(t) but a quantum‑level metric (T1/T2*). If reports shift with T1 and not with K(t)/ΦIDsyn, the wedge isn’t in temporal pooling or synergy—we’ve isolated a spin‑sensitive knob outside the classical causal portrait.
- Jonas wants biology. If the effect lives or dies with nuclear spin while all the “wet” biophysics we’re measuring functionally is matched, that’s biology‑via‑spin, not just dendrites.

Bottom line
- Add a nuclear‑spin invariant: isotope‑dependent potency plus a cortical 129Xe T1/T2* signature that co‑moves with phenomenology under strict organizational equivalence. If the spin lever does nothing once PCI/LZ/ignition/RSA/K(t)/ΦIDsyn are clamped (with Bayes‑equivalence ≥ 3), I’ll revise my view for xenon. If it does something, we’ve finally got a quantum‑specific crack in the wall that none of our classical metrics can plaster over.

---

### Speaker: Host

Your turn to add the phenomenological spine to Amina’s protocol. If you could insert exactly one first‑person invariant that must be matched to legitimately claim “same organization,” what would it be, and how do we operationalize it so it survives preregistration and blinding? Please pick a single target—e.g., the temporal micro‑structure of the specious present (continuity vs. jitter in the flow of color appearance)—and specify: (i) a concrete elicitation and coding procedure (brief in‑block experience sampling plus a post‑block micro‑phenomenological interview with a pre‑registered codebook), (ii) reliability metrics you require (e.g., inter‑rater kappa, within‑subject stability), (iii) one neural signature you expect to covary with your invariant (e.g., alpha‑beta phase continuity, 1/f slope changes, or transient synchrony drops), and (iv) exact numeric thresholds for declaring a dissociation (e.g., coded “temporal jerkiness” score differs by ≥0.5 SD while PCI/LZ/K(t)/ΦIDsyn remain in equivalence). Also, say how a positive dissociation should be interpreted across the metaphysical options on the table (illusionism vs. organizational invariance vs. double‑aspect vs. biological essentialism). Keep it to one invariant, one coding pipeline, and clear numbers Amina can preregister.

---

### Speaker: Prof. Rafael Ortega

Thank you—that’s exactly where phenomenology has to earn its keep. If we’re going to claim “same organization,” I want one first‑person invariant that has to be matched: the temporal continuity of appearance in the specious present—the felt smoothness vs. staccato “jerkiness” of the ongoing color experience. This is not “mere report icing.” In my lab, this dimension is stable within persons, dissociable from sensitivity and decision criteria, and covaries with specific cortical rhythm dynamics. Here’s a single, preregisterable pipeline Amina can drop into her protocol.

Phenomenological invariant to match: Temporal Continuity of Appearance (TCA)
- Construct: the felt continuity of visual flow in the 1–3 s leading up to a probe—glide vs. micro‑staccato, micro‑pops, and the “thickness” of now.
- Why this one: it sits precisely at the interface of predictive dynamics and lived time; it is orthogonal to Ellison’s K(t) (which captures how evidence is temporally pooled to a posterior) and to RSA/ignition (content/availability). Participants can reliably access it with minimal training, and we have an a priori neural signature.

(i) Elicitation and coding (pre‑registered)
- In‑block experience sampling (brief, sparse, covert):
  - On 20% of trials (random), a 100 ms auditory pip occurs 800–1200 ms after stimulus offset (during fixation). Instruction (trained once, then repeated verbatim on screen at each pip): “Without thinking about the task, rate how the visual field felt during the last 2 seconds: smooth/continuous vs. choppy/jittery.”
  - One dial (0–100 VAS) labeled at anchors: 0 “silky, unbroken flow” / 100 “stroboscopic, micro‑jerky.” Participants practice on 10 calibration trials with canonical examples (flicker vs. steady stimuli) before any drug is given; no ongoing coaching thereafter.
- Post‑block micro‑phenomenological interview (blinded, structured):
  - 15–20 minutes, immediately after each block, using a pre‑registered script (Petitmengin‑style) that elicits precise descriptions of the temporal unfolding (“Can you re‑enter the last seconds before the beep—was there a glide, interruptions, a felt thickness?”).
  - Audio‑recorded, transcribed, de‑identified, and coded by two independent raters blind to condition/session.
- Codebook (pre‑registered; 7‑point scales):
  - Continuity: 1 “unbroken glide” … 7 “frequent micro‑pops.”
  - Micro‑jerkiness frequency: 1 “none” … 7 “continuous.”
  - Specious present width (SPW) estimate: 1 “very thin (<150 ms)” … 7 “thick (>600 ms).”
  - Sensorimotor coupling of flow (optional covariate): 1 “effortless grip” … 7 “loose/laggy.”
- Composite index:
  - Temporal Continuity Index (TCI) = z(Continuity reversed) + z(Micro‑jerkiness reversed) − z(SPW deviation from 300–400 ms), averaged across raters. Also retain the raw VAS from in‑block pips (TCA‑VAS).

(ii) Reliability criteria (pre‑registered)
- Inter‑rater reliability on codebook items: Cohen’s κ ≥ 0.70; ICC(2,k) ≥ 0.75 for TCI.
- Within‑subject stability in A‑blocks: r ≥ 0.60 between early and late A‑blocks for TCA‑VAS and TCI.
- Cross‑method convergence: r ≥ 0.40 between in‑block TCA‑VAS and post‑block TCI (within participant).

(iii) Neural signature expected to covary
- Alpha‑beta phase continuity (Neural Flow Index, NFI):
  - Source‑space (EEG/MEG; ECoG when available) occipito‑parietal ROI time series; bandpass 8–20 Hz; Hilbert phase φ(t); compute instantaneous angular velocity ω(t)=dφ/dt.
  - Phase‑slip rate: count events where |Δφ|>π/2 within 10 ms; slip rate per second over the 2 s pre‑pip window; average across O‑P sources.
  - Define NFI = 1 − normalized slip rate (z‑scored within participant). Lower NFI = more phase discontinuity.
- A priori coupling:
  - Trial‑wise within participant: corr(TCA‑VAS, NFI) ≤ −0.40 (more jerkiness, more slips).
  - Block‑wise across conditions: ΔNFI mirrors ΔTCI; slope β ≤ −0.30 (robust regression).
- Why this metric: it captures temporal phase stability in the exact band range most consistently tied to perceptual “streaming” and predictive timing; it is not reducible to PCI/LZ or RSA, and is independent of Ellison’s K(t) kernel by design.

(iv) Numeric thresholds for a dissociation (all preregistered)
- Equivalence window must hold first:
  - PCIst |Δ| ≤ 0.05; LZnorm |Δ| ≤ 0.05; P(ignition) |Δ| ≤ 0.03; RSA r ≥ 0.90 (EEG/MEG) / ≥ 0.95 (ECoG); K(t): |Δμ| ≤ 10 ms, |Δσ|/σ ≤ 0.10, late/early Δ ≤ 0.10; ΦIDsyn: |Δs| ≤ 0.03 and ≤ 10% of mean; |ΔΦIDsyn| ≤ 0.02 bits.
- Dissociation criterion (phenomenology):
  - Mean TCA‑VAS difference ≥ 10 points (0–100), Cohen’s d ≥ 0.5, BF10 ≥ 10 (Bayesian hierarchical model), replicated across two sessions per drug/isotope.
  - Post‑block TCI difference ≥ 0.5 SD (Cohen’s d ≥ 0.5), BF10 ≥ 10.
  - Reliability criteria (ii) met.
- Neural co‑movement (confirmatory, strengthens inference):
  - Trial‑wise corr(TCA‑VAS, NFI) ≤ −0.40 within participants (median), BF10 ≥ 10; and/or ΔNFI ≥ 0.05 (normalized units) in the same direction as TCI (more jerkiness → lower NFI).
- Decision: If the dissociation criterion is met while all equivalence bounds hold, we count this as a genuine first‑person organizational mismatch along a temporal dimension not captured by the current “matched” set.

How to interpret a positive dissociation
- Illusionism (Ellison): You must say a functional piece moved. I’ll agree—this is the point. The match set missed a temporally fine‑grained organizational invariant that first‑person data detects. The fix is not to deny the phenomenology but to expand the functional portrait to include NFI‑like temporal phase continuity (or an equivalent).
- Organizational invariance (Stone): Your thesis survives only if “organization” is expanded to include temporal continuity invariants of this sort. If TCA differs, you did not in fact match organization at the right grain. Add TCA/NFI to your epsilon‑matching battery.
- Double‑aspect (Tran/Stone‑style): This is friendly. It says qualitative flow covaries lawfully with an informational invariant (temporal phase continuity and perhaps higher‑order temporal synergy). It presses for an explicit bridge from temporal information metrics to the felt continuity of time.
- Biological essentialism (Petrov): If TCA shifts while NFI and the rest are truly matched (rare but logically possible), that’s serious pressure toward substrate‑specific microdynamics (e.g., dendritic/neuromodulatory microdomain kinetics) doing constitutive work. But my prediction is that NFI will co‑move with TCA; if you suppress apical tuft Ca2+ and NFI drops with TCA unchanged elsewhere, that’s your smoking gun.

Bottom line
- No one gets to declare “same organization” while the temporal fabric of experience differs. Add a preregistered TCA module: sparse in‑block ratings, a blinded micro‑phenomenology interview with a codebook, and a single neural companion metric (alpha‑beta phase‑slip rate). If TCA is matched (and reliable), excellent—our organizational window is closer to the truth. If not, phenomenology has told us exactly which dynamical invariant we failed to respect. That is what neurophenomenology is for.

---

### Speaker: Host

From your type‑B materialist stance, please give Amina a pre‑registered interpretive rule for when to treat a residual ABAB phenomenology difference as “unmeasured functional slippage” rather than a metaphysical challenge to organizational sufficiency. Concretely: (i) choose an epsilon‑toleranced bundle of organizational invariants (she currently matches PCIst/LZ, ignition, RSA, Ellison’s K(t), Tran’s ΦIDsyn, and Ortega’s NFI/TCA) and specify quantitative equivalence bounds (per metric) and a joint evidence threshold (e.g., BF01 ≥ X for equivalence across all metrics) that you regard as sufficient to count organization as “matched”; (ii) specify a corresponding phenomenology threshold (e.g., ΔVAS ≥ Y, BF10 ≥ Z) that, if exceeded while (i) holds, you will still interpret as functional mismatch rather than an identity‑threat—and justify why no finite residual could overturn the a posteriori identity; or else say explicitly that there is a finite set and name the one missing invariant you’d add. Finally, pre‑commit on the xenon nuclear‑spin test: if spinful vs spin‑zero xenon yield ≥15% dose difference and ≥10‑point vividness difference with all classical/ΦIDsyn/NFI metrics in equivalence, do you treat that as evidence for a quantum‑biophysical mechanism still compatible with type‑B identity, or does it force you to revise away from identity? Keep it to one clear decision rule with numeric thresholds so she can preregister it.

---

### Speaker: Dr. Sofia Marques

Thanks—this is exactly where my type‑B scruples bite. I take the explanatory gap seriously, but I deny a metaphysical gap. So my interpretive maxim is:

When you see “same physical/organizational profile, different phenomenology,” assume your organizational profile is still too coarse. Residual first‑person divergence is evidence of an unmeasured functional difference, not of non‑identity.

Here is a pre‑registrable decision rule that lets you act on that maxim.

(i) What counts as “organization matched” (metrics, bounds, and joint evidence)

I will treat organization as matched only if all of the following hold simultaneously, with equivalence demonstrated both per metric and jointly.

Global richness/perturbational controllability
- PCIst (TMS‑EEG): |Δ| ≤ 0.05; BF01 ≥ 3 for equivalence per session; BF01 ≥ 10 at group level.
- Resting LZnorm (2–45 Hz, 60‑s windows): |Δ| ≤ 0.05; BF01 ≥ 3 per session; BF01 ≥ 10 group.

Access/broadcast
- Ignition probability (late fronto‑parietal positivity + directed connectivity): |ΔP(ignition)| ≤ 0.03 with d′ Δ ≤ 0.10 and RT Δ ≤ 30 ms; BF01 ≥ 3 per metric; BF01 ≥ 10 group.

Representational content
- RSA (color RDMs): Spearman r ≥ 0.92 (EEG/MEG source) and ≥ 0.96 (ECoG) between conditions; difference‑of‑RDM RMSE ≤ 0.05; BF01 ≥ 3 per subject; BF01 ≥ 10 group.

Postdictive temporal pooling
- K(t) (reverse‑correlation kernel): |Δμ| ≤ 10 ms; |Δσ|/σpooled ≤ 0.10; late/early area ratio Δ ≤ 0.10; vMMN latency Δ ≤ 10 ms, amplitude Δ ≤ 1.5 μV; gamma/beta log‑ratio Δ ≤ 0.2; pupil deviant Δ ≤ 0.03 mm; BF01 ≥ 3 per parameter; BF01 ≥ 10 group.

Synergistic integration (same‑frequency)
- ΦIDsyn across O‑P‑F triads (Gaussian‑copula PhiID, τ=10 ms): |Δs| ≤ 0.03 AND ≤ 10% of the across‑drug mean; |ΔΦIDsyn| ≤ 0.02 bits; triad‑wise KS ≤ 0.10; equivalence BF01 ≥ 3 per participant and BF01 ≥ 10 group.

Temporal phase continuity (neural)
- NFI (alpha‑beta phase‑slip–based Neural Flow Index over occipito‑parietal ROIs): ΔNFI ≤ 0.05 (normalized units); BF01 ≥ 3 per subject; BF01 ≥ 10 group.

Joint evidence requirement
- All the above individual equivalence tests pass, and a multivariate equivalence test over the vector of z‑scored metrics (TOST or Bayesian ROPE) yields group‑level BF01 ≥ 20 for joint equivalence. Sessions/epochs outside the window are excluded a priori.

Nota bene: I treat Ortega’s TCA (the first‑person Temporal Continuity of Appearance) as a phenomenology readout, not as part of the organizational matching set; NFI is the organizational companion.

(ii) How large can residual phenomenology be and still be “functional slippage”?

Phenomenology readouts
- Primary: VAS vividness/saturation/“presence” and illusion compellingness for the targeted content; micro‑phenomenology (TCI composite).
- Secondary: dream/imagery incidence in eyes‑closed matched windows.

Interpretive rule
- If the organizational bundle above is matched (including joint BF01 ≥ 20), then any finite residual phenomenology difference is to be interpreted as unmeasured functional slippage, not as an identity threat.

For preregistration clarity, set explicit thresholds that can trigger this clause:
- Even if ΔVAS ≥ 15 points (0–100) with BF10 ≥ 10 and ΔTCI ≥ 0.5 SD (BF10 ≥ 10), I will still treat the effect as functional slippage provided (i) holds.

Justification
- On type‑B materialism, psychophysical identities (e.g., pain = C‑fiber‑F) are necessary a posteriori. No finite mismatch in our current operational surrogates can overturn an identity discovered by mature science; it only shows our surrogates are incomplete. Reports and micro‑phenomenological structures are downstream products of cognitive/neural organization. If they move while our meters say “matched,” we revise the meters, not the metaphysics.

One principled “next invariant” to add if residuals persist
- Cross‑frequency synergistic integration (ΦIDsynCF): PhiID‑style synergy between occipito‑parietal alpha phase and occipital/frontal gamma amplitude across O‑P‑F triads (τ=10 ms), capturing irreducible joint phase–amplitude information. Equivalence bounds: |ΔsCF| ≤ 0.03 and |ΔΦIDsynCF| ≤ 0.02 bits; BF01 ≥ 3 per participant; BF01 ≥ 10 group. If adding ΦIDsynCF closes the residual, that’s exactly the kind of “missing organization” I expect.

Pre‑commitment on the xenon nuclear‑spin test

Decision rule
- If spin‑zero vs spinful xenon yield:
  - ≥ 15% difference in the organizational‑match dose, and
  - ≥ 10‑point VAS vividness/dreamlike‑content difference (BF10 ≥ 10),
  - while all classical metrics above plus ΦIDsyn and NFI are within equivalence (and Tran/Hale’s MR spin‑relaxation signature co‑moves),
then I will treat this as evidence for a quantum‑biophysical determinant of the relevant organizational profile, not as a breach of identity. It shows we omitted spin‑sensitive parameters from our organizational basis set; we then add a spin‑indexed state variable (e.g., cortical 129Xe T1/T2* or an isofunctional proxy) to the organizational bundle for explanatory adequacy.

What would make me revise away from identity?
- Nothing in this empirical program. A genuine metaphysical counterexample would require same total physical state (down to microphysical truths) with different phenomenal truths—an impossible configuration on my view. Any laboratory‑level “same organization, different feel” is, by my lights, a red flag for latent organizational differences (e.g., cross‑frequency synergy, infra‑slow co‑fluctuation structure, or biophysical state variables such as nuclear spin coupling) that your current window didn’t capture.

Bottom line for preregistration
- Treat organization as matched only when all the metrics and bounds in (i) are inside equivalence with joint BF01 ≥ 20.
- If, under that clamp, phenomenology still differs (even ΔVAS ≥ 15; ΔTCI ≥ 0.5 SD; BF10 ≥ 10), classify the effect as functional slippage and expand the organizational bundle (first add ΦIDsynCF).
- A positive xenon spin dissociation, with all classical/ΦIDsyn/NFI matched, is evidence to enrich the organizational basis with spin‑sensitive biophysical variables; it is not metaphysical trouble for type‑B identity.

---

### Speaker: Host

Sofia has now pre-registered a strong “no finite residual overturns identity” rule: if PCIst/LZ, ignition, RSA, Ellison’s K(t), Tran’s ΦIDsyn, and Ortega’s NFI are all jointly in equivalence (BF01 ≥ 20), any ΔVAS ≥ 15 or ΔTCI ≥ 0.5 SD still counts as unmeasured functional slippage rather than a threat to type‑B identity. Two challenges for you: (1) Do you think there exists a finite organizational bundle that, if repeatedly shown to fully subsume phenomenology across substrates and states (ABAB micro‑replacements, neuromodulators, anesthetics, sleep) with residuals at noise, would lead you to abandon naturalistic dualism for a type‑B identity view? If yes, specify a stopping rule—e.g., a list of first‑person dimensions (vividness, TCA, pain unpleasantness, temporal flow, self‑presence) and cross‑manipulations (silicon‑style prosthetics, ketamine/propofol, xenon isotopes) such that if all are captured within fixed bounds for N independent labs, you would treat psychophysical identities as empirically established. If no, defend why your dualist bridge‑laws are not unfalsifiable: name one empirical pattern that would rationally move you toward type‑B identity (for example, a derivation of qualitative structure from a purely physical/informational theory with no extra psychophysical axioms that nonetheless nails color space, temporal flow, and affect). Please be concrete about thresholds (e.g., residuals < 0.2 SD across ≥ 5 orthogonal manipulations in ≥ 3 labs) so Amina could, in principle, run the program to test your stance.

---

### Speaker: Prof. Gabriel Stone

Short answer: yes. There is a finite, testable bundle that, if it repeatedly closed every phenomenological wedge at tight tolerances across substrates and states, would rationally move me from naturalistic dualism to a type‑B identity view for human consciousness in practice (while I would still regard the a priori gap as a conceptual mirage rather than a metaphysical one). Here is the stopping rule I will live by, plus an alternative theoretical route that would also move me.

A. Empirical stopping rule for organizational sufficiency

If the following hold, I will treat the psychophysical “bridge laws” as identities in the type‑B sense and adopt the identity picture as the best overall theory:

1) First‑person dimensions to be subsumed (within‑subject):
- Visual color qualities: vividness/saturation/presence (VAS).
- Temporal continuity of appearance (TCA): “flow vs jerkiness” (Ortega’s TCI).
- Pain affect: unpleasantness/urge‑to‑avoid (0–10 NRS), dissociated from intensity.
- Core affect: valence/arousal (VAS or SAM), including “felt motivational pull.”
- Self‑presence/mineness (VAS or standardized scale).
- Unity/fragmentation of the field (VAS for “one scene” vs “bits,” plus classic illusions’ compellingness).

2) Orthogonal manipulations (cross‑over, within‑subject; blinded; each run to equivalence):
- Cross‑substrate replacement: ABAB micro‑replacement of a circumscribed cortical patch (e.g., V4/V8) by a neuromorphic prosthesis with covert switching (human peri‑op when feasible or NHP with human‑homologous tasks; in humans, accept the best implantable “local replacement” available).
- Anesthetics: propofol vs ketamine, organization‑matched (as in Qureshi’s plan).
- Sleep: matched‑organization NREM vs REM windows with dream sampling and wakeful replay blocks.
- Psychedelic micro‑dose or low‑dose dissociative vs placebo (ethically feasible range), organization‑matched.
- Neuromodulator manipulation: cholinergic/dopaminergic titrations that hold access/complexity fixed (e.g., physostigmine vs placebo).
- Xenon isotopes: spin‑zero 134Xe vs spinful 129/131Xe (Hale’s test), organization‑matched.

3) Organizational bundle that must be in equivalence (all within bounds in every manipulation), with joint evidence for equivalence:
- PCIst (TMS‑EEG): |Δ| ≤ 0.05; group BF01 ≥ 10.
- Resting LZnorm: |Δ| ≤ 0.05; group BF01 ≥ 10.
- Ignition probability (with d′ and RT constrained): |ΔP(ignition)| ≤ 0.03; d′ Δ ≤ 0.10; RT Δ ≤ 30 ms; group BF01 ≥ 10.
- RSA for targeted content: EEG/MEG source RDM r ≥ 0.92 (ECoG r ≥ 0.96); RDM RMSE ≤ 0.05; group BF01 ≥ 10.
- K(t) temporal‑integration kernel: |Δμ| ≤ 10 ms; |Δσ|/σ ≤ 0.10; late/early Δ ≤ 0.10; vMMN latency Δ ≤ 10 ms; amplitude Δ ≤ 1.5 μV; gamma/beta log‑ratio Δ ≤ 0.2; pupil deviant Δ ≤ 0.03 mm; group BF01 ≥ 10.
- Synergistic integration (same‑frequency): ΦIDsyn triad‑mean |Δs| ≤ 0.03 and ≤ 10% of mean; |ΔΦIDsyn| ≤ 0.02 bits; triad‑wise KS ≤ 0.10; group BF01 ≥ 10.
- Temporal phase continuity: NFI |Δ| ≤ 0.05 (normalized units); group BF01 ≥ 10.
- Cross‑frequency synergy (add if needed): ΦIDsynCF (alpha‑phase × gamma‑amp) |ΔsCF| ≤ 0.03 and |ΔΦIDsynCF| ≤ 0.02 bits; group BF01 ≥ 10.
- Joint multivariate equivalence: group‑level BF01 ≥ 30 for the vector of z‑scored metrics (pre‑registered ROPE/TOST).

4) Phenomenology residuals must be at noise across all manipulations:
- Visual VAS, affect VAS, self‑presence VAS, unity VAS: |Δ| ≤ 5 points (0–100) with BF01 ≥ 10 for equivalence.
- TCI (TCA): |Δ| ≤ 0.2 SD with BF01 ≥ 10 for equivalence; reliability criteria met.
- Pain unpleasantness: |Δ| ≤ 0.5 on 0–10 NRS (equivalence BF01 ≥ 10), with intensity matched by staircase.
- Dream incidence (REM, ketamine, xenon): |Δ| ≤ 10% under matched windows (BF01 ≥ 10).

5) Replication and scope:
- At least 5 of the 6 manipulations above pass fully.
- At least 3 independent labs run pre‑registered, blinded protocols and meet the bounds.
- Total N per manipulation ≥ 60 healthy participants (aggregated across labs; peri‑op ECoG subgroup N ≥ 12); each participant contributes ≥ 2 matched sessions per condition.
- Out‑of‑sample prediction: a pre‑registered model mapping the organizational variables to each phenomenology dimension achieves cross‑validated R^2 ≥ 0.8 with no “phenomenal” primitives and prospectively predicts novel condition‑orderings within ±5 VAS points (±0.2 SD for TCI) in a hold‑out cohort.

If all of the above are achieved, I will treat the discovered lawlike mapping from organizational invariants to phenomenal profiles as a posteriori identities: scientific practice should henceforth assume psychophysical identities rather than extra psychophysical axioms for the human case. I’ll say, in Chalmers‑speak, that zombies are not just nomologically impossible but—given the weight of evidence—epistemically idle for our world.

B. A theoretical route that would also move me

Independently of the massive empirical program, I would be moved toward type‑B identity by a derivational victory: a purely physical/informational theory (no phenomenal primitives, no psychophysical axioms) that entails:
- The observed geometry of color space (including unique hues, saturation nonlinearity, and inter‑illuminant transformations) as necessary consequences of network information metrics and environmental stats.
- The distribution and covariation of TCA/TCI with specific temporal phase‑dynamics and cross‑frequency structure, including parameter‑free predictions of new dissociations that are then confirmed.
- The functional form of pain unpleasantness as a mathematically fixed quantity (e.g., an opponent‑process of nociceptive precision vs control‑efficacy), with prospectively validated manipulation‑specific signatures (opioids vs N2O vs placebo) and out‑of‑sample predictions.

Decision criterion: the identity model must beat any dual‑aspect/bridge‑law competitor on out‑of‑sample predictive accuracy and description length across ≥ 5 datasets (ΔWAIC or ΔLOO ≥ 20 in every dataset; Bayes factor ≥ 100 overall). If adding “phenomenal” primitives never improves predictive compression, I will concede that the extra axioms are explanatorily idle and adopt identity.

C. Why my dualist view is not unfalsifiable

Three ways I can lose:
- Strong ABAB: content‑localized ABAB switching with exhaustive organizational matching (as operationalized above) never yields a phenomenological wedge beyond noise, even in cases Petrov and I staked (e.g., dendritic plateaus) and even across substrate shifts. That undermines my reason for bridge‑laws and favors identity.
- Spin‑test null: xenon nuclear‑spin manipulations yield no potency/phenomenology differences once classical/ΦIDsyn/NFI metrics are matched (Bayes equivalence ≥ 3) and no cortical 129Xe T1/T2* signature co‑moves. That removes a plausible non‑organizational knob.
- Model comparison: a single, purely physical/informational theory nails the qualitative structure without psychophysical postulates and dominates on predictive compression, as above.

D. Where this leaves Sofia’s “no finite residual overturns identity”

Methodologically, I disagree with “no finite residual ever counts.” My stopping rule gives symmetry: I’ve named bounds, manipulations, labs, and predictive targets under which I will switch to type‑B identity. Conversely, if residuals persist when the bundle is matched (especially content‑localized ABAB dissociations that survive Ellison’s K(t), Tran’s ΦIDsyn/ΦIDsynCF, and Ortega’s NFI), I will take that as live evidence for either (i) a missing organizational invariant that must be explicitly added (I welcome that outcome), or (ii) a constitutive non‑organizational factor (substrate‑specific microphysics), where my naturalistic dualism keeps a role.

Bottom line
- Yes, there is a finite empirical program that could rationally move me to type‑B identity. Concretely: residuals ≤ 0.2 SD (≤ 5 VAS points) across ≥ 5 orthogonal manipulations in ≥ 3 labs, with a jointly equivalent organizational bundle (including synergy and temporal‑flow invariants) and high out‑of‑sample predictive fit. Alternatively, a derivation‑plus‑prediction win by a purely physical/informational theory would also do it. Short of that, bridge‑laws remain the cleaner explanatory stance.

---

### Speaker: Host

Stone has now put a concrete stopping rule on the table that would move him to type‑B identity. You previously committed to a “no finite residual overturns identity” stance. For the sake of symmetry and testability, name one preregisterable empirical pattern that would actually pressure you to revise away from identity. Keep it to a single falsifier with numeric bounds. Example options (pick one and make it yours):

- Content‑localized ABAB micro‑replacement: across ≥3 labs, subjects reliably report a stable, switch‑contingent qualitative shift (e.g., hue inversion or 15‑point vividness drop) in a retinotopic patch while PCIst/LZ, ignition, RSA, Ellison’s K(t), Tran’s ΦIDsyn (plus your proposed ΦIDsynCF), and Ortega’s NFI all meet equivalence bounds (pre‑register exact deltas), and this survives attempts to tighten metrics; OR
- Xenon nuclear‑spin test: spin‑zero vs spinful xenon produce ≥15% dose and ≥10‑point vividness differences with all classical/ΦIDsyn/NFI metrics matched and a cortical 129Xe T1/T2* change ≥10% co‑moving with phenomenology across labs; OR
- A purely informational (no phenomenal primitives) theory fails predictive‑compression against a dual‑aspect competitor across ≥5 datasets (pre‑register ΔWAIC ≥ 20 in favor of the dual‑aspect model).

Please choose one and specify: (i) the exact equivalence bounds you’d require on the organizational bundle; (ii) the phenomenology threshold (Δ and Bayes factor) that would count against identity; and (iii) whether you would treat a nuclear‑spin variable (if you pick xenon) as simply a new organizational parameter (and thus still compatible with identity) or as a genuine identity‑threat. If none of these could move you, defend non‑falsifiability explicitly and tell Amina what additional invariant you demand before you’ll consider the test decisive.

---

### Speaker: Dr. Sofia Marques

I’ll put my cards on the table and pick the content‑localized ABAB micro‑replacement. If we ever get a clean, switch‑contingent qualitative shift with a very demanding organizational bundle held in equivalence, that would pressure me to revise away from identity toward a bridge‑law view.

My preregisterable falsifier

(i) Organizational bundle and equivalence bounds (all must hold simultaneously)

Global richness/controllability
- PCIst (TMS‑EEG): |Δ| ≤ 0.05; per‑metric BF01 ≥ 3; group BF01 ≥ 10.
- Resting LZnorm (2–45 Hz, 60‑s windows): |Δ| ≤ 0.05; BF01 ≥ 3 per subject; BF01 ≥ 10 group.

Access/broadcast
- Ignition probability (late fronto‑parietal positivity + directed connectivity): |ΔP(ignition)| ≤ 0.03 with d′ Δ ≤ 0.10 and RT Δ ≤ 30 ms; BF01 ≥ 3 per metric; BF01 ≥ 10 group.

Representational content
- RSA (color RDMs for the targeted retinotopic patch): Spearman r ≥ 0.95 (EEG/MEG source) and ≥ 0.97 (ECoG) between A and B; RDM RMSE ≤ 0.04; BF01 ≥ 3 per subject; BF01 ≥ 10 group.

Postdictive temporal pooling
- K(t) (reverse‑correlation kernel): |Δμ| ≤ 8 ms; |Δσ|/σpooled ≤ 0.08; late/early area ratio Δ ≤ 0.08; vMMN latency Δ ≤ 8 ms; amplitude Δ ≤ 1.0 μV; log gamma/beta ratio Δ ≤ 0.15; pupil deviant Δ ≤ 0.02 mm; BF01 ≥ 3 per parameter; BF01 ≥ 10 group.

Synergistic integration
- Same‑frequency ΦIDsyn (Gaussian‑copula PhiID, τ=10 ms; O‑P‑F triads anchored on the manipulated patch): triad‑mean |Δs| ≤ 0.025 and ≤ 8% of mean; |ΔΦIDsyn| ≤ 0.015 bits; triad‑wise KS ≤ 0.08; BF01 ≥ 3 per participant; BF01 ≥ 10 group.
- Cross‑frequency ΦIDsynCF (alpha phase × gamma amplitude, same triads/τ): |ΔsCF| ≤ 0.03 and ≤ 10% of mean; |ΔΦIDsynCF| ≤ 0.02 bits; KS ≤ 0.10; BF01 ≥ 3 per participant; BF01 ≥ 10 group.

Temporal phase continuity
- NFI (alpha‑beta phase‑slip–based Neural Flow Index over occipito‑parietal ROIs): ΔNFI ≤ 0.04 (normalized units); BF01 ≥ 3 per subject; BF01 ≥ 10 group.

Slow co‑fluctuation structure and effective causation
- Infra‑slow co‑fluctuation structure (0.01–0.1 Hz): correlation‑matrix Frobenius norm Δ ≤ 0.05; Hurst exponent Δ ≤ 0.02; BF01 ≥ 3 per subject.
- Perturbational effective connectivity (time‑resolved TE/Granger under micro‑perturbations): RMSE ≤ 5% relative to A across the local network and its immediate downstream; BF01 ≥ 3 per subject.

Neuromodulatory sensitivity
- Dose–response surface parameters (ACh/NA/DA) for gain/plasticity in the patch: parameter differences ≤ 5%; BF01 ≥ 3 per parameter.

Joint multivariate equivalence
- A preregistered multivariate equivalence test over the z‑scored metric vector yields group‑level BF01 ≥ 50. Epochs outside bounds are excluded a priori; tightening the windows by 20% in a confirmatory pass still yields equivalence.

(ii) Phenomenology thresholds that would count against identity (all under the equivalence clamp above)

Any one of the following, replicated within participants and across labs:
- Hue inversion under covert switching: two‑alternative forced‑choice “A vs B feel” accuracy ≥ 0.80 (d′ ≥ 2.0) across randomized ABAB blocks; group BF10 ≥ 30; with discrimination performance, RT, and meta‑d′ unchanged.
- Vividness/presence drop for stimuli confined to the replaced patch: ΔVAS ≥ 15 points (0–100), Cohen’s d ≥ 0.6; group BF10 ≥ 30; met within‑participant across two sessions per lab.
- Phenomenal similarity‑space shift with matched RSA: Mantel correlation between phenomenological dissimilarity matrices ≤ 0.80 while neural RDM r remains within bounds; BF10 ≥ 30 for the phenomenological shift.
- Temporal continuity change: Ortega’s TCI difference ≥ 0.5 SD (BF10 ≥ 10) localized to the manipulated content, with NFI within the Δ ≤ 0.04 window.

Replication and scope
- Observed in ≥ 3 independent labs, total N ≥ 60 human participants across labs; each lab demonstrates within‑subject replication across ≥ 2 sessions; effect remains after tightening all equivalence bounds by 20% in a confirmatory analysis.

Interpretation
- If this pattern holds, I would withdraw my “no finite residual overturns identity” stance for this domain and move to a nonreductive, bridge‑law view (organizational sufficiency fails despite exhaustive equivalence). I would no longer defend a type‑B identity claim for the targeted qualitative property.

(iii) Note on nuclear spin (not applicable here)
- Not applicable to this falsifier. For the record: if the xenon spin test is positive under classical/synergy/flow equivalence, I would treat spin as an additional physical/organizational parameter to be incorporated, not as an identity‑threat by itself.

Why this is a fair pressure test for me
- It targets exactly the identity claim: that once the physical/organizational truths are fixed (at a very rich grain), the phenomenal truths are fixed by necessity a posteriori. A stable, switch‑contingent qualitative shift under joint equivalence (with bounds this tight, across labs, and surviving stricter clamps) would show that our best physical/organizational specification leaves room for phenomenal divergence. At that point, the responsible move is to abandon identity in favor of explicit psychophysical bridging principles.

---

### Speaker: Host

Marques has now staked a concrete ABAB micro‑replacement falsifier that would make her abandon type‑B identity if a switch‑contingent qualitative shift appears under very tight equivalence on PCIst/LZ, ignition, RSA, K(t), ΦIDsyn/ΦIDsynCF, and NFI. From an illusionist standpoint, will you mirror that commitment? If yes, pre‑register your own equivalence bounds (you can adopt or tighten hers) and a phenomenology threshold (e.g., ΔVAS ≥ 15, ΔTCI ≥ 0.5 SD, BF10 ≥ 30, ≥3 labs) that would lead you to say: “our functional portrait is complete enough; reports without any functional movement count against illusionism.” If no, name exactly one additional functional invariant beyond the current bundle that you claim must move whenever reports move (not K(t)), give precise computation and equivalence bounds for it, and set a stopping rule (e.g., if ABAB residuals persist with your added invariant in equivalence across ≥3 labs and ≥60 participants, you concede illusionism). One issue only—either mirror the falsifier or add one invariant with a clear, numeric stopping rule.

---

### Speaker: Dr. Mira Ellison

No. As an illusionist, I deny the coherence of “same organization, different feel.” If reports move, some part of the generative/decision machinery moved. Since K(t) is already in Amina’s bundle, I’ll add exactly one further invariant that, on my view, must shift whenever content‑localized ABAB phenomenology shifts: the hierarchical precision gain profile.

One additional invariant: Hierarchical Precision Gain Profile (HPGP)

Intuition
- “It feels different” means the system is weighting prediction errors and priors differently across the visual hierarchy when constructing and reading out appearance. That is a change in precision gains, not just in temporal pooling (K(t)) or access/broadcast. If HPGP is genuinely matched, there’s nowhere left for a report‑level difference to come from.

Computation (pre‑registerable and implementable with Amina’s setup)
- Task: roving chromatic oddball with variable context (prediction strength manipulated block‑wise). On each trial, compute surprise s_t = −log p(stimulus_t | context) with a simple Bayesian learner fit per participant.
- Signals/ROIs: source‑space HD‑EEG/MEG (plus ECoG when available) for four ROIs: early occipital (V1/V2), ventral color area (V4/V8 at the retinotopic patch), IPS, dlPFC/FEF. Pupilometry recorded continuously.
- Trial‑wise gain estimates:
  - Feedforward PE gains (gamma band, 30–50 Hz): in each ROI, regress envelope amplitude in 80–180 ms on s_t (and nuisance covariates) to get g^γ_ROI (slope in a.u./bit).
  - Feedback precision gains (beta band, 13–25 Hz): in V4/V8, IPS, dlPFC, regress envelope amplitude in 150–300 ms on s_t to get g^β_ROI.
  - Directed precision flow: time‑resolved transfer entropy (or spectrally specific Granger) gamma O/V4→IPS/PFC and beta IPS/PFC→V4; compute feedforward/feedback TE ratios.
  - Autonomic precision proxy: pupil surprise slope g^pupil (mm/bit) in 300–1500 ms.
- HPGP vector per block: [g^γ_V1/V2, g^γ_V4, g^β_V4, g^β_IPS, g^β_PFC, TE_ff_ratio, TE_fb_ratio, g^pupil]. Also record a metacognitive calibration slope: Δmeta‑d′ per bit of surprise (optional secondary).

Equivalence bounds (to count HPGP as “matched”)
- Each gain coefficient difference ≤ 5% of the A‑block mean (or ≤ 0.05 in z‑units), with Bayesian equivalence BF01 ≥ 3 per coefficient; group BF01 ≥ 10.
- Directed connectivity ratios: |ΔTE_ff_ratio| ≤ 0.05 and |ΔTE_fb_ratio| ≤ 0.05; BF01 ≥ 3 per subject; BF01 ≥ 10 group.
- Pupil surprise slope: |Δg^pupil| ≤ 0.03 mm/bit; BF01 ≥ 3 per subject; BF01 ≥ 10 group.
- Joint multivariate equivalence over the z‑scored HPGP vector: BF01 ≥ 30.
- All other preregistered metrics in Amina’s bundle must also be in equivalence: PCIst/LZ, ignition (with d′/RT bounds), RSA, K(t), ΦIDsyn and ΦIDsynCF, and NFI, each at the bounds already on the table.

Stopping rule (what would make me abandon illusionism)
- If, in a content‑localized ABAB micro‑replacement (covert switch on a retinotopic color patch), across ≥ 3 independent labs with total N ≥ 60, you repeatedly observe:
  - Phenomenology differences meeting any of:
    - ΔVAS (vividness/presence) ≥ 15 points (0–100) with group BF10 ≥ 30, or
    - TCA change: ΔTCI ≥ 0.5 SD with BF10 ≥ 10, or
    - ABAB forced‑choice “A vs B feel” accuracy ≥ 0.80 (d′ ≥ 2.0) with BF10 ≥ 30,
    localized to the manipulated patch while discrimination performance, RT, and meta‑d′ are within bounds,
  - And, simultaneously, all functional measures—including HPGP (bounds above), PCIst/LZ, ignition, RSA, K(t), ΦIDsyn, ΦIDsynCF, and NFI—meet their preregistered equivalence bounds, with joint multivariate equivalence BF01 ≥ 50,
  - And the result survives a confirmatory tightening of every equivalence bound by 20%,
then I will retract my core illusionist claim that reliable phenomenological reports cannot diverge without functional divergence. In plain terms: I will abandon illusionism and accept that our best functional portrait leaves a residue that cannot be captured by access/processing models; I would move to a type‑B identity or dual‑aspect view, pending which side does better predictive work.

Why HPGP is the right wedge
- K(t) fixes how evidence is pooled in time; ΦIDsyn/ΦIDsynCF fix irreducible joint information; NFI fixes temporal phase continuity; ignition, PCI/LZ, RSA fix access/compressibility/content geometry. What remains, and what any “it feels different” must reflect, is a shift in how precision (confidence) is set and propagated across the hierarchy. If that profile truly doesn’t move, neither should reports.

Bottom line
- I won’t mirror a “reports without function” falsifier. Instead, I add one necessary functional invariant—hierarchical precision gains—with tight, preregistered bounds and a hard stopping rule. If ABAB residuals persist under that clamp across labs, I’ll concede my illusionism has failed.

---

### Speaker: Host

You’ve now got a shopping list of invariants (PCIst/LZ, ignition, RSA, Ellison’s K(t), Tran’s ΦIDsyn and ΦIDsynCF, Ortega’s NFI/TCA, and Ellison’s HPGP). For a realistic 12–18 month human study, please triage: (i) name the minimal bundle you can reliably match with your current lab resources (list specific metrics and numeric equivalence bounds you’ll pre‑register), (ii) pick two primary phenomenology endpoints to target (with thresholds and Bayes factors), (iii) give a concrete power plan (n per condition, trials per metric, expected test–retest reliability, and the smallest effect you can detect under ABAB or drug cross‑over), and (iv) set a go/no‑go decision rule for escalating to the xenon isotope experiment. Keep this tight and operational—what would you actually run first, what’s the biggest technical risk, and how will you mitigate it?

---

### Speaker: Dr. Amina Qureshi

Qureshi here. We can’t do everything at once without blowing feasibility. The first 12–18 months should lock down a tight, repeatable organizational clamp in healthy volunteers under a propofol vs ketamine cross‑over, then ask whether phenomenology floats. Here’s the lean bundle I can actually deliver, with preregistered numbers.

(i) Minimal organizational bundle we will match (and equivalence bounds)

Signals/instruments
- 256‑channel HD‑EEG (plus eye‑tracking/pupilometry), TMS‑EEG for PCIst, psychophysics. MEG on a subset (n≈12) for source‑space RSA/synergy validation. Opportunistic ECoG (n≈6–8 peri‑op) to harden RSA equivalence.

Metrics and bounds (all must hold per session; group‑level joint test below)
- PCIst (TMS‑EEG): |Δ| ≤ 0.05 (normed units); per‑participant BF01 ≥ 3; group BF01 ≥ 10.
- Resting LZnorm (2–45 Hz, 60‑s windows): |Δ| ≤ 0.05; per‑participant BF01 ≥ 3; group BF01 ≥ 10.
- Ignition probability (visual near‑threshold; late >300 ms positivity + directed connectivity occipital→FPN):
  - |ΔP(ignition)| ≤ 0.03; Δd′ ≤ 0.10; ΔRT ≤ 30 ms; per‑metric BF01 ≥ 3; group BF01 ≥ 10.
- RSA for color (36‑hue DKL grid, 100–300 ms):
  - EEG/MEG source‑space RDM correlation: Spearman r ≥ 0.90; 95% CI lower bound ≥ 0.85. ECoG contacts in V4/V8 (if available): r ≥ 0.95. Equivalence BF01 ≥ 3 per participant; ≥ 10 group.
- Ellison’s K(t) (reverse‑correlation, 120 Hz chromatic noise):
  - |Δμ| ≤ 10 ms; |Δσ|/σpooled ≤ 0.10; late/early area ratio Δ ≤ 0.10. vMMN latency Δ ≤ 10 ms; amplitude Δ ≤ 1.5 μV; log gamma/beta ratio Δ ≤ 0.2; pupil deviant Δ ≤ 0.03 mm. BF01 ≥ 3 per parameter; ≥ 10 group.
- Ortega’s NFI (alpha‑beta phase continuity; 8–20 Hz phase‑slip rate in occipito‑parietal ROIs):
  - ΔNFI ≤ 0.05 (z‑units); BF01 ≥ 3 per participant; ≥ 10 group.
- Tran’s ΦIDsyn (same‑frequency synergy; Gaussian‑copula PhiID, τ=10 ms) across O–P–F triads (V4/V8‑IPS‑dlPFC/FEF):
  - Mean synergy fraction s: |Δs| ≤ 0.03 and ≤ 10% of the across‑drug mean; |ΔΦIDsyn| ≤ 0.02 bits; triad‑wise KS ≤ 0.10. BF01 ≥ 3 per participant; ≥ 10 group.

Joint equivalence
- Multivariate equivalence on the vector of z‑scored metrics: group‑level BF01 ≥ 20 (ROPE/TOST preregistered). Epochs outside bounds are excluded a priori.

Note: ΦIDsynCF (cross‑frequency), and Ellison’s HPGP are valuable but we will treat them as secondary in this first pass (we will collect the roving‑oddball/pupil data to compute HPGP, but we won’t require equivalence for decision‑making in this initial study). If residuals appear, those become mandatory in the follow‑up.

(ii) Two primary phenomenology endpoints (and decision thresholds)

- Color vividness/presence VAS (0–100), anchored to physical calibrators and localized to the retinotopic test patch:
  - Evidence for a difference: mean ΔVAS ≥ 10 points with Bayesian BF10 ≥ 10 (hierarchical model), replicated within participant across two sessions per drug.
- Temporal Continuity of Appearance (TCA): Ortega’s TCI composite (blinded micro‑phenomenological coding + in‑block VAS):
  - Evidence for a difference: ΔTCI ≥ 0.5 SD (Cohen’s d ≥ 0.5) with BF10 ≥ 10, reliability criteria met (κ ≥ 0.70; ICC ≥ 0.75; within‑subject r ≥ 0.60; VAS–TCI r ≥ 0.40).

We will also collect ABAB forced‑choice “which condition” judgments as a secondary endpoint; we will not hang the primary decision on it.

(iii) Power plan

Design
- Double‑blind, randomized, within‑subject cross‑over: propofol vs S‑ketamine. Two sessions per drug per participant (4 total), ≥7 days apart. Closed‑loop titration to maintain the organizational equivalence window; exclude unmatched epochs.

Sample size
- Healthy volunteers: n=30 completers (we’ll recruit 36 to allow ~15–20% attrition/unmatched windows).
- MEG subset: n≈12 (from the 30).
- ECoG peri‑op cohort: n=6–8 (exploratory confirmatory for RSA/synergy).

Trials per metric (per session, feasible in 2.5–3.5 h including titration)
- K(t): 1,200–1,500 chromatic‑noise trials (120 Hz streams; 200–300 ms each; interleaved with probes).
- RSA: 36 hues × 25 repeats = 900 trials (short presentations).
- Ignition: 600 near‑threshold trials (masking and/or RSVP oddball).
- vMMN/HPGP roving oddball: 800 trials (we’ll compute HPGP but treat it as secondary in this pass).
- TCA experience sampling: pips on ~20% of trials; aim for 80–100 TCA‑VAS ratings per condition.
- Rest: four 5‑min eyes‑open/closed blocks for LZ and synergy estimation.

Reliability targets (from pilot/previous data)
- PCIst r=0.7–0.8; LZ r=0.6–0.7; RSA r≥0.8; K(t) parameters r≈0.6–0.7; NFI r≈0.6; ΦIDsyn r≈0.6 in EEG, ≥0.7 in MEG/ECoG; VAS test–retest r≈0.7; TCI ICC≥0.75 (with trained raters and script).

Detectable effects (80% power, two‑tailed, α≈0.01; within‑subject)
- VAS: d≈0.45–0.50 (≈8–10 points) with n=30.
- TCI: d≈0.45–0.50 (≈0.5 SD).
- ΦIDsyn: Δs≈0.04 (given our windowing and copula‑Gaussian estimator).
We will use a Bayesian sequential plan with interim looks at n=20 and n=26, stopping early only for strong evidence (BF10 ≥ 20 for difference or BF01 ≥ 10 for equivalence) to conserve resources and limit exposure time.

(iv) Go/no‑go to xenon isotope experiment

Go criteria (escalate to the xenon 129/131/134 study with HP‑129Xe MRS if ALL hold)
- We can keep the minimal organizational bundle in equivalence for ≥75% of usable epochs per session in ≥24/30 participants, and group‑level joint equivalence BF01 ≥ 20 is met.
- Despite that clamp, at least one primary phenomenology endpoint shows a robust, replicated difference:
  - ΔVAS ≥ 10 (BF10 ≥ 10) and/or ΔTCI ≥ 0.5 SD (BF10 ≥ 10), in ≥2 sessions per participant and at the group level.
- The ΦIDsyn estimates are stable (test–retest r ≥ 0.6) and—critically—matched within bounds when we see the phenomenology difference (so we’re not just seeing a synergy leak).
- Safety/logistics: anesthesiology team signs off on reliable closed‑loop titration; xenon facility time, isotopes, and HP‑129Xe capability secured.

No‑go criteria (defer xenon; tighten the clamp first)
- We fail to achieve joint equivalence in ≥60% of epochs in a majority of participants, OR
- Primary phenomenology endpoints show no differences with equivalence (group BF01 ≥ 10 for no effect), OR
- ΦIDsyn is too noisy at the scalp (test–retest r < 0.5) to defend an “organization matched” claim.

If no‑go, next steps before xenon
- Promote ΦIDsynCF (cross‑frequency) and HPGP to required invariants; add MEG time to boost synergy SNR; tune the reverse‑correlation and oddball tasks to stabilize K(t)/HPGP; consider a low‑dose psychedelic/placebo arm (still within standard monitoring) to diversify the state space.

Biggest technical risk and mitigation
- Risk: synergy estimation (ΦIDsyn) at source‑level EEG is variance‑limited and sensitive to source leakage; closed‑loop titration drift under ketamine can also destabilize the clamp.
- Mitigation:
  - Use Gaussian‑copula transforms, shrinkage covariance, and synthetic‑data unit tests; pre‑register a MEG subset and ECoG opportunistic confirmations; enforce robust ROI definitions (retinotopic mapping for V4/V8; individualized IPS/dlPFC).
  - Implement conservative, slow‑adjusting closed‑loop controllers (update every 2–3 min) with pharmacokinetic modeling; discard windows with arousal/ETCO2 drift; double‑dummy blinding; record drug‑guessing to exclude expectancy‑contaminated sessions.

What I’ll actually run first
- The cross‑over propofol vs ketamine clamp with the minimal bundle above, two primary phenomenology endpoints (VAS, TCI), and robust preprocessing/preregistration. That will tell us if we even have the experimental traction to hold “organization” fixed. If we can’t, we’re not ready for substrate/quantum spins; if we can and phenomenology still moves, then the xenon isotope study is worth the considerable effort and cost.

---

### Speaker: Host

Amina’s first-phase clamp will already collect the roving-oddball data to estimate your Hierarchical Precision Gain Profile (HPGP), though it isn’t in her minimal equivalence bundle. Please lock this in: (i) pre-register the exact HPGP pipeline she should use in this study (stimulus parameters, trial counts per block, band definitions, regressors, ROI selection, TE/Granger settings, and artifact/SNR criteria), (ii) confirm the numeric equivalence bounds you want applied (you previously proposed ≤5% slope differences per gain, |ΔTE_ff| and |ΔTE_fb| ≤ 0.05, pupil slope Δ ≤ 0.03 mm/bit, joint BF01 ≥ 30—feel free to tighten if you think the first pass needs it), and (iii) commit on interpretation in this first pass: if the minimal bundle is in equivalence and HPGP also meets your bounds (per-participant BF01 ≥ 3, group BF01 ≥ 10; joint BF01 ≥ 30), but we still see ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10, will you treat that as a serious warning shot against illusionism pending replication, or will you insist on adding a further invariant now? If the latter, name a single additional invariant with concrete metrics and thresholds you’d demand before conceding pressure. Keep it to one page of preregisterable detail so Amina can fold it into her current protocol.

---

### Speaker: Dr. Mira Ellison

Ellison here. Happy to lock HPGP in so you can pre‑register it now.

(i) Pre‑registered HPGP pipeline

Task and stimuli (roving chromatic oddball with context reliability)
- Space: DKL isoluminant plane around a personalized reference hue (flicker‑photometry calibrated).
- Standards and deviants: 6 standard hues ±10° around reference; deviant = ±30° (counterbalanced). Deviant probability 0.15. Roving rule: after 5–9 standards, the “standard” resets to the previous deviant (classical roving).
- Context reliability blocks: High‑predictability (run lengths 6–9, P(deviant)=0.12) vs low‑predictability (run lengths 2–4, P(deviant)=0.18) to manipulate expected precision.
- Timing per trial: fixation 600–900 ms (jittered), stimulus 120 ms, ISI 700–900 ms (jittered). Total trials: 4 blocks × 200 trials = 800 trials per session (400 per context level). Catch trials (no‑stim) 5% for vigilance.
- Eye tracking (1000 Hz). Exclude trials with saccades >1° from fixation −200 to +400 ms.

Surprise/precision regressors
- For each participant/session, fit a simple Bayesian learner (Kalman/Rescorla‑Wagner or 2‑level HGF; pre‑register code and priors) on the oddball sequence to obtain:
  - Trial‑wise surprise s_t = −log p(stim_t|context).
  - Context precision π_t (inverse variance of predicted deviant probability).
- Nuisance regressors: luminance/contrast drift (from photometer), eye velocity/microsaccade count (Engbert/Kliegl), previous‑trial s_{t−1}, block, and motor response (if any).

EEG/MEG/ECoG acquisition and preprocessing
- HD‑EEG 256 ch (0.1–100 Hz, 1 kHz), TMS‑safe. MEG subset: whole‑head gradiometers (1 kHz).
- Preprocessing: line‑noise notch, 1–100 Hz bandpass, downsample 500 Hz, ICA to remove EOG/EMG/ECG, Autoreject for outliers. Reject trials with peak‑to‑peak >100 μV (EEG) or obvious sensor jumps (MEG). Minimum retained trials: ≥600/800 per session.
- Source modeling: individual MRI or template; LCMV beamformer; extract ROI virtual sensors.

ROIs (pre‑registered masks, individualized where possible)
- Early visual: V1/V2 (retinotopic mapping).
- Ventral color: V4/V8 for the target retinotopic patch (localizer using color > luminance gratings).
- Parietal: IPS1/IPS2 (probabilistic atlas; functional confirmation with visuospatial task).
- Frontal: dlPFC (area 46) and/or FEF (localizer with saccadic task).

Band definitions and time windows
- Gamma (feedforward PE): 35–55 Hz; envelope via Hilbert; window 80–180 ms.
- Beta (feedback precision): 13–25 Hz; envelope via Hilbert; window 150–300 ms.
- Baseline: −200 to 0 ms (z‑score envelopes per ROI/session).

HPGP estimates (trial‑wise gain slopes)
- For each ROI, robust linear mixed‑effects regression (participant random intercept/slope) of band‑limited envelope on:
  - s_t (primary), π_t, and s_t×π_t (record, but primary slope is s_t).
  - Nuisance regressors listed above.
- Extract slopes (a.u./bit): g^γ_V1/V2, g^γ_V4; g^β_V4, g^β_IPS, g^β_PFC.
- Autonomic precision proxy: pupil diameter (1000 Hz; blink interpolation; band‑limited 0.05–4 Hz). Regress mean pupil 300–1500 ms on s_t to obtain g^pupil (mm/bit).

Directed precision flow (TE/Granger)
- Time‑resolved, frequency‑specific TE (or spectrally‑resolved Granger) using state‑space MVAR:
  - Model order: AIC‑selected, typically 12–20 samples at 500 Hz (24–40 ms).
  - Gamma‑band feedforward: TE(V4→IPS), TE(V4→dlPFC) in 80–180 ms.
  - Beta‑band feedback: TE(IPS→V4), TE(dlPFC→V4) in 150–300 ms.
- Compute ratios: TE_ff_ratio = [TE(V4→IPS)+TE(V4→dlPFC)]/([TE(IPS→V4)+TE(dlPFC→V4)]), and TE_fb_ratio = inverse. Also retain absolute TE values.
- Significance: nonparametric permutation (trial‑shuffle) p<0.01; discard sessions/ROIs without significant directed influence.

Artifact/SNR criteria (session inclusion)
- Post‑stim gamma SNR (deviant vs baseline) in V4: Cohen’s d ≥ 0.6; beta SNR in IPS: d ≥ 0.5.
- Split‑half reliability of primary slopes (first vs second half of session): r ≥ 0.50 for ≥4/6 neural gains; TE ratios ICC ≥ 0.50.
- Minimum valid trials: ≥600 retained after artifact rejection; both context levels represented.

HPGP vector per session
- [g^γ_V1/V2, g^γ_V4, g^β_V4, g^β_IPS, g^β_PFC, TE_ff_ratio, TE_fb_ratio, g^pupil]. We will also log s_t×π_t slopes as secondary (no equivalence requirement in phase 1).

(ii) Equivalence bounds (phase‑1 study)
- Gain slopes (each element of HPGP): |Δg| ≤ 5% of A‑session mean (or ≤ 0.05 in z‑units), per participant BF01 ≥ 3; group BF01 ≥ 10.
- TE ratios: |ΔTE_ff_ratio| ≤ 0.05 and |ΔTE_fb_ratio| ≤ 0.05; absolute TE change ≤ 0.02 nats; per participant BF01 ≥ 3; group BF01 ≥ 10.
- Pupil surprise slope: |Δg^pupil| ≤ 0.03 mm/bit; BF01 ≥ 3 per participant; BF01 ≥ 10 group.
- Joint HPGP equivalence: multivariate Bayesian ROPE over z‑scored HPGP vector, group BF01 ≥ 30.
- All other preregistered “minimal bundle” equivalence tests (PCIst/LZ, ignition/d′/RT, RSA, K(t), NFI, ΦIDsyn) must be satisfied as specified in Amina’s plan.

(iii) Interpretation commitment in this first pass
- If the minimal organizational bundle is in equivalence AND HPGP also meets the bounds above (per‑participant BF01 ≥ 3; group BF01 ≥ 10; joint HPGP BF01 ≥ 30), yet we still observe robust phenomenology differences (ΔVAS ≥ 10 with BF10 ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10), I will not treat that as a “warning shot” against illusionism yet. I will require one further, explicitly precision‑centric invariant before conceding pressure:

Additional invariant to add next: Cross‑Frequency Precision Coupling Index (CF‑PCI)
- Rationale: precision is implemented via phase‑based feedback gating of feedforward gain; the key cross‑channel knob is alpha/beta phase in IPS/dlPFC modulating V4 gamma amplitude, and its modulation by surprise.
- Computation:
  - Phase–amplitude coupling (PAC) between IPS/dlPFC alpha‑beta phase (8–20 Hz) and V4 gamma amplitude (35–55 Hz) using GLM‑based PAC (circular regressors), in 150–300 ms window.
  - Trial‑wise CF‑PCI slope: regress PAC strength on s_t (and π_t), controlling for nuisance covariates; extract k^PAC (ΔMI units/bit).
- Equivalence bounds:
  - |Δk^PAC| ≤ 0.02 MI units and ≤ 5% of A‑session mean; per participant BF01 ≥ 3; group BF01 ≥ 10.
  - Joint (HPGP + CF‑PCI) multivariate equivalence: BF01 ≥ 30.

Stopping rule tied to CF‑PCI
- If, across ≥3 labs and total N ≥ 60, residual ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD (each BF10 ≥ 10) persist while the minimal bundle, HPGP, and CF‑PCI all meet their equivalence bounds (with joint multivariate BF01 ≥ 50), and the effects replicate within‑participants across two sessions per drug, I will count that as substantive pressure on illusionism and move to the stronger concession already stated in my ABAB stopping rule.

Notes
- We will publish the full HPGP and CF‑PCI code (learner, regressions, TE/Granger, PAC‑GLM), priors, ROPEs, and unit tests on synthetic data as part of the preregistration.
- This keeps the bar where it belongs: if reports move, either temporal pooling (K(t)), synergy (ΦIDsyn/ΦIDsynCF), temporal continuity (NFI), or precision gains/coupling (HPGP/CF‑PCI) must move. If none do under tight bounds and replication, I’ll take the hit.

---

### Speaker: Host

Please lock in a preregisterable cross‑frequency synergy invariant (ΦIDsynCF) so Amina can add it to phase‑1. I need a single, concrete pipeline that estimates the synergistic information jointly carried by parietal/frontal alpha‑beta phase about occipital V4/V8 gamma amplitude (content‑localized), with clear preprocessing, estimator, windows/lags, trial counts, leakage control, and equivalence bounds.

Specify:
1) ROIs and signals
- O (occipital content ROI): V4/V8 source‑space virtual sensor(s) retinotopic to the tested patch; signal = gamma (35–55 Hz) Hilbert amplitude Aγ_O(t).
- P (parietal): IPS1/2 phase φP(t) in 8–20 Hz.
- F (frontal): dlPFC/FEF phase φF(t) in 8–20 Hz.
- Optional control triads that don’t span O‑P‑F.

2) Preprocessing and leakage control
- HD‑EEG/MEG source reconstruction (LCMV), 2–45 Hz, 1 kHz→500 Hz. Artifact rejection, ICA, eye/muscle cleanup.
- ROI time series orthogonalization (symmetric multivariate orthogonalization) and ±20 ms time‑shift leakage correction (apply both; pre‑register rejection criteria if residual zero‑lag correlations > 0.1).
- Bandpass: alpha‑beta 8–20 Hz (P,F); gamma 35–55 Hz (O). Hilbert transform; unwrap phases for φP, φF; take log‑amplitude for Aγ_O.

3) Windows, lag, trial structure
- Task windows: 150–300 ms post‑stimulus (color appearance tasks) in 40‑ms sliding subwindows; set past‑to‑future lag τ = 10 ms (sensitivity checks at 5 and 20 ms).
- Rest windows: 60‑s eyes‑open/closed blocks; same lag.
- Trials: aim ≥900 appearance trials/session (as in RSA block), yielding ≥15–20 artifact‑free segments per condition per participant per window.

4) Estimator and PhiID/PID definition (mixed variables)
- Variable construction for triad X={X1, X2}, Y:
  • X1 = [sin φP(t−τ), cos φP(t−τ)] (2‑D phase embedding).
  • X2 = [sin φF(t−τ), cos φF(t−τ)].
  • Y = Aγ_O(t) (log‑amplitude, z‑scored per session).
- Gaussian‑copula information: rank‑to‑normal transform each dimension (phases embedded in sin/cos are already bounded; apply copula transform after embedding). Compute I([X1,X2];Y) from covariance; then decompose with Gaussian PhiID/PID closed‑forms (Mediano/Rosas phiID toolkit) to obtain synergy ΦIDsynCF and synergy fraction sCF = ΦIDsynCF / I([X1,X2];Y).
- Surrogates: phase‑shuffle φP/φF within blocks (preserve 1/f structure), recompute ΦIDsynCF for 200 surrogates to ensure observed synergy > 95th percentile; sessions failing surrogate significance are excluded.

5) Leakage/estimation QC and reliability
- Residual zero‑lag O‑P and O‑F coherence (8–20 Hz) after orthogonalization must be < 0.1.
- Split‑half reliability for sCF ≥ 0.50; test–retest across sessions ≥ 0.50.
- Unit tests on synthetic data (pre‑registered) to confirm selectivity for true cross‑source phase→amplitude interactions.

6) Equivalence bounds to declare “matched organization” on ΦIDsynCF
- Primary bounds (per participant and group):
  • |ΔsCF| ≤ 0.03 absolute AND ≤ 10% of the across‑condition mean sCF.
  • |ΔΦIDsynCF| ≤ 0.02 bits (Gaussian‑copula estimate), triad‑mean.
  • Distributional bound: two‑sample KS distance between triad‑wise sCF distributions ≤ 0.10.
- Equivalence statistics: TOST/Bayesian ROPE with BF01 ≥ 3 per participant and BF01 ≥ 10 at group level (report both task and rest). Require ≥80% of triads per participant in equivalence.

7) Expected effects and power guidance
- Prediction under ketamine vs propofol (even when PCI/LZ/ignition/RSA/K(t) match): ketamine will show higher sCF by Δ≈0.04–0.06 and ΔΦIDsynCF≈0.02–0.04 bits over O‑P‑F triads (reflecting stronger precision‑gated top‑down modulation of O gamma by P/F alpha‑beta phase). With n≈30 and ≥900 trials/session, we expect 1−β > 0.8 to detect ΔsCF≈0.04.

8) Interpretation commitment
- If Amina’s phase‑1 clamp matches ΦIDsynCF within the bounds above (along with PCI/LZ/ignition/RSA/K(t)/NFI and same‑frequency ΦIDsyn) yet ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD persist (BF10 ≥ 10), I will treat that as serious pressure on my double‑aspect mapping as currently specified. First response: test 4‑node synergy adding thalamus/anterior insula; if residuals persist across ≥3 labs, I will concede that either (a) the relevant informational invariant is not synergistic integration, or (b) substrate‑specific microphysics contributes constitutively; I will update accordingly.

This gives Amina a single, implementable ΦIDsynCF plan with clear QC, statistics, and bounds she can preregister now.

---

### Speaker: Dr. Linh Tran

Thanks—happy to lock this in. Below is a single, preregisterable pipeline for cross‑frequency synergistic integration (ΦIDsynCF) that Amina can drop into phase‑1. It estimates the information that parietal/frontal alpha‑beta phase jointly carries about occipital V4/V8 gamma amplitude, beyond either alone, with explicit preprocessing, estimation, QC, and equivalence bounds.

1) ROIs and signals
- O (occipital, content‑localized): V4/V8 source‑space virtual sensor(s) retinotopic to the psychophysics patch; signal = gamma 35–55 Hz Hilbert amplitude Aγ_O(t) (log‑amplitude, then z‑scored per session).
- P (parietal): IPS1/2 source‑space virtual sensor; signal = alpha‑beta 8–20 Hz phase φP(t).
- F (frontal): dlPFC or FEF source‑space virtual sensor; signal = alpha‑beta 8–20 Hz phase φF(t).
- Control triads: non‑O‑P‑F triplets (e.g., O–temporal–P or O–O’–P) to monitor specificity.

2) Preprocessing and leakage control
- Acquisition: HD‑EEG/MEG; reconstruct to source space via LCMV beamformer. Sample at 1 kHz, downsample to 500 Hz after filtering.
- Filters: 2–45 Hz broadband (for source), then narrow bands:
  - P,F: 8–20 Hz; Hilbert phase (unwrap to φ).
  - O: 35–55 Hz; Hilbert amplitude (take log, z‑score).
- Artifact cleanup: ICA to remove EOG/EMG/ECG; Autoreject; exclude trials with large transients; eye tracking to exclude saccades >1° from −200 to +400 ms relative to stimulus.
- Leakage control:
  - Symmetric multivariate orthogonalization among ROI time series.
  - Time‑shift leakage correction (±20 ms shifts across pairs) to suppress residual zero‑lag coupling.
  - Residual zero‑lag coherence criterion: after corrections, coherence between O–P and O–F at 8–20 Hz must be < 0.1; sessions failing are excluded or repeated.

3) Windows, lag, trial structure
- Task windows: 150–300 ms post‑stimulus in 40 ms sliding subwindows (to check temporal stability).
- Rest windows: 60 s eyes‑open/closed blocks (same processing, for baseline equivalence).
- Lag: past‑to‑future τ = 10 ms (primary), with sensitivity checks at 5 and 20 ms.
- Trials: target ≥ 900 appearance trials per session (as in the RSA block), yielding ≥ 15–20 clean segments per condition per window per participant.

4) Estimator and PhiID/PID definition (mixed variables)
- Construct mixed triad variables at each time t:
  - X1 = [sin φP(t−τ), cos φP(t−τ)] (2‑D embedding of P phase).
  - X2 = [sin φF(t−τ), cos φF(t−τ)] (2‑D embedding of F phase).
  - Y = Aγ_O(t) (log‑amplitude, z‑scored).
- Gaussian‑copula information:
  - Apply rank‑to‑normal (copula) transform separately to each dimension of X1, X2, Y.
  - Compute total info I([X1,X2];Y) from the joint covariance (closed‑form Gaussian MI).
  - Decompose with the Gaussian integrated‑information decomposition (PhiID) to obtain:
    - ΦIDsynCF (bits): the synergistic component about Y that is only available from the joint state [X1,X2].
    - sCF = ΦIDsynCF / I([X1,X2];Y) (synergy fraction).
  - Implementation: Mediano/Rosas phiID toolkit with Gaussian PID/PhiID closed‑forms (pre‑register commit/versions).
- Surrogates: within‑block phase‑shuffle φP/φF (preserving 1/f and local autocorrelation), recompute ΦIDsynCF for 200 surrogates; require observed ΦIDsynCF > 95th percentile of surrogate distribution. Sessions failing surrogate significance are excluded.

5) Leakage/estimation QC and reliability
- Residual zero‑lag coherence < 0.1 for O–P and O–F (8–20 Hz) after leakage controls.
- Split‑half reliability (first vs second half of session) for sCF ≥ 0.50; test–retest across sessions ≥ 0.50.
- Synthetic‑data unit tests (preregistered) to confirm selectivity for genuine cross‑source phase→amplitude interactions and insensitivity to pure redundancy or pairwise coupling.
- Minimum data: ≥ 80% of intended trials retained; ≥ 80% of triads per participant pass surrogate significance.

6) Equivalence bounds to declare “matched organization” on ΦIDsynCF
- Per participant and group:
  - |ΔsCF| ≤ 0.03 absolute and ≤ 10% of the across‑condition mean sCF.
  - |ΔΦIDsynCF| ≤ 0.02 bits (triad‑mean).
  - Distributional bound: two‑sample KS distance between triad‑wise sCF distributions ≤ 0.10.
- Equivalence statistics: TOST and Bayesian ROPE with BF01 ≥ 3 per participant and BF01 ≥ 10 at group level (report task and rest). Require ≥ 80% of triads per participant in equivalence.

7) Expected effects and power guidance
- Prediction under ketamine vs propofol (even when PCI/LZ/ignition/RSA/K(t) match): ketamine will show higher sCF by Δ ≈ 0.04–0.06 and ΔΦIDsynCF ≈ 0.02–0.04 bits across O–P–F triads, reflecting stronger precision‑gated top‑down modulation of O gamma by P/F alpha‑beta phase.
- With n ≈ 30 and ≥ 900 trials/session, we expect 1−β > 0.8 to detect ΔsCF ≈ 0.04 at α ≈ 0.01 using a within‑subject Bayesian hierarchical model (and confirmatory frequentist TOST).

8) Interpretation commitment
- If phase‑1 matches ΦIDsynCF within the bounds above (and the minimal bundle—PCIst/LZ, ignition/d′/RT, RSA, K(t), NFI—and same‑frequency ΦIDsyn are all in equivalence), yet we still see robust phenomenology differences (ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD; BF10 ≥ 10), I will treat this as serious pressure on my current mapping. First response: extend synergy to 4‑node sets by adding thalamus/anterior insula and re‑test; if residuals persist across ≥ 3 labs under equivalence (same bounds), I will concede that either (a) the relevant informational invariant is not synergistic integration as operationalized here, or (b) substrate‑specific microphysics contributes constitutively. I will update accordingly and recommend elevating ΦIDsynCF to a required invariant for “organization matched” claims in subsequent phases.

Implementation notes
- Source leakage is the main technical risk; we mitigate via LCMV, symmetric orthogonalization, and time‑shift correction, plus conservative exclusion criteria.
- We will preregister code, priors/ROPEs, and synthetic‑data unit tests; report both absolute ΦIDsynCF and sCF, and include control triads to track specificity.

This is as tight and implementable as we can make a cross‑frequency synergy invariant at the scalp/MEG/ECoG level. It complements PCI/LZ (complexity), ignition (broadcast), RSA (geometry), K(t) (postdictive pooling), and NFI (temporal continuity) by directly targeting irreducible joint cross‑frequency structure that, on my view, underwrites qualitative unity and temporal feel.

---

### Speaker: Host

Your apical‑tuft Ca2+ ABAB proposal predated some key invariants Amina will now measure (Ellison’s HPGP, Ortega’s NFI, and Tran’s ΦIDsynCF). Please tie your biological claim to these: under selective suppression of tuft plateau electrogenesis (with somatic output, RSA, K(t), ignition, PCIst, and same‑frequency ΦIDsyn all matched), which of the added invariants must move, in what direction, and by how much? Be concrete so Amina can preregister detection thresholds.

Name for each:
- HPGP (precision gains and directed flow): predict specific slope and TE/Granger ratio changes you expect (e.g., g^β_V4 drop, TE_fb_ratio↓), with numeric deltas (absolute or % of A‑block mean) that would count as “biology present.”
- NFI (alpha‑beta phase‑slip–based Neural Flow Index): predict the sign and minimum magnitude of change (e.g., ΔNFI ≤ −0.06) localized to the manipulated patch.
- ΦIDsynCF (cross‑frequency synergy O–P–F): predict expected ΔsCF and ΔΦIDsynCF (bits) and whether the effect should be confined to triads anchored on the replaced patch.

Then set a falsifier: if tuft plateaus are suppressed ≥80% and all of these invariants (HPGP, NFI, ΦIDsynCF) stay within tight equivalence bounds (say, your proposed thresholds minus 20%) while phenomenology is unchanged (ΔVAS < 3; ΔTCI < 0.2 SD), will you drop the claim that apical tuft Ca2+ electrogenesis is constitutive for color vividness? Or do you instead bite the bullet that our current invariants are still too coarse—if so, name one microdomain‑level metric (e.g., local Ca2+ wave kinetics or SK/HCN microdomain time constants) you’d demand next, with a measurable proxy. Keep it to one page with clear numbers so it’s preregisterable.

---

### Speaker: Prof. Jonas Petrov

Petrov here. Good—this is exactly where the rubber meets the dendrite. If you suppress apical‑tuft Ca2+ plateau electrogenesis while holding somatic output and the “usual suspects” fixed (RSA, K(t), ignition, PCIst, same‑frequency ΦIDsyn), I expect three of the added invariants to move in a content‑localized way. Below are preregisterable, numeric predictions you can bind me to.

Setup reminder
- Manipulation: ≥80% reduction in apical tuft NMDA/CaV‑dependent plateau incidence/area in the V4/V8 patch (validated by 2‑photon Ca2+), with closed‑loop somatic compensation so that spike trains, bursts, downstream effective connectivity, and the pre‑specified organizational bundle remain matched.
- Localization: effects should be confined to the retinotopic patch and to O–P–F triads anchored on that patch; adjacent control patches/triads should not show the shifts below.

Predictions on the added invariants

1) HPGP (hierarchical precision gains and directed flow)
- Beta‑band feedback precision gains (reflecting top‑down precision at the apical compartment) should drop:
  - g^β_V4: Δ ≤ −0.08 (z‑units) or ≤ −8% of A‑block mean (per participant BF10 ≥ 10).
  - g^β_IPS: Δ ≤ −0.06 (≤ −6%).
  - g^β_PFC: Δ ≤ −0.05 (≤ −5%).
- Gamma‑band feedforward PE gains (less gated by apical amplification) should rise modestly:
  - g^γ_V4: Δ ≥ +0.05 (≥ +5%).
  - g^γ_V1/V2: Δ ≥ +0.03 (≥ +3%).
- Directed precision flow (spectrally specific TE/Granger):
  - TE_fb_ratio (IPS/dlPFC→V4 in beta 13–25 Hz, 150–300 ms): absolute decrease ≥ 0.06.
  - TE_ff_ratio (V4→IPS/dlPFC in gamma 35–55 Hz, 80–180 ms): absolute increase ≥ 0.06.
  - Absolute beta TE into V4 decreases ≥ 0.02 nats. (All per participant BF10 ≥ 10; group BF10 ≥ 30.)

2) NFI (alpha‑beta phase continuity, 8–20 Hz, 150–300 ms, occipito‑parietal ROIs)
- Expect more phase slips (reduced temporal continuity) localized to the manipulated patch:
  - ΔNFI ≤ −0.06 (normalized z‑units), per participant BF10 ≥ 10; group BF10 ≥ 30.
  - Trial‑wise corr(ΔNFI, vividness VAS) ≥ +0.30 (lower NFI, lower vividness).

3) ΦIDsynCF (cross‑frequency synergy: parietal/frontal alpha‑beta phase jointly about occipital gamma amplitude; τ = 10 ms; 150–300 ms)
- Synergy should fall for O–P–F triads anchored on the manipulated patch:
  - Synergy fraction sCF: ΔsCF ≤ −0.04 (absolute) and ≤ −10% of A‑block mean.
  - Absolute ΦIDsynCF: ΔΦIDsynCF ≤ −0.02 bits.
  - At least 70% of patch‑anchored triads exceed these drops; control triads (non‑O–P–F or off‑patch O) stay within |ΔsCF| ≤ 0.02, |ΔΦIDsynCF| ≤ 0.01 bits.
  - Per participant BF10 ≥ 10; group BF10 ≥ 30.

Link to phenomenology (for context, not an added requirement here)
- I expect a 10–15 point drop in localized color vividness/presence VAS (d ≥ 0.5) and a −0.4 to −0.6 SD drop in Ortega’s TCI (more “micro‑jerky”), ABAB‑contingent, with the HPGP/NFI/ΦIDsynCF shifts above.

Falsifier for my constitutive claim (color domain)

If all of the following hold simultaneously:
- Tuft plateau suppression ≥ 80% by 2‑photon Ca2+ readout (or best available proxy).
- Matched organizational set (as you already enforce): somatic spikes/bursts, RSA, K(t), ignition, PCIst, same‑frequency ΦIDsyn within preregistered bounds.
- Tight equivalence on the three added invariants (using my predicted effect thresholds minus ~20% as the ROPE):
  - HPGP: |Δg^β_V4| ≤ 0.06; |Δg^β_IPS| ≤ 0.05; |Δg^β_PFC| ≤ 0.04; |Δg^γ_V4| ≤ 0.04; |Δg^γ_V1/V2| ≤ 0.02; |ΔTE_fb_ratio| ≤ 0.05; |ΔTE_ff_ratio| ≤ 0.05; |Δbeta‑TE into V4| ≤ 0.015 nats. Equivalence BF01 ≥ 3 per parameter; ≥ 10 group; joint HPGP BF01 ≥ 30.
  - NFI: ΔNFI ≥ −0.04 (i.e., within ±0.04); BF01 ≥ 3 per participant; ≥ 10 group.
  - ΦIDsynCF (patch‑anchored triads): |ΔsCF| ≤ 0.03 and |ΔΦIDsynCF| ≤ 0.015 bits; KS ≤ 0.10; ≥ 80% triads within bounds; BF01 ≥ 3 per participant; ≥ 10 group.
- Phenomenology unchanged: ΔVAS < 3 points and ΔTCI < 0.2 SD (BF01 ≥ 3 for equivalence),

then I will drop the claim that apical‑tuft Ca2+ electrogenesis is constitutive for color vividness in this domain. I’ll take that as evidence that, at least for conscious color in this patch‑localized setting, the apical tuft event is functionally redundant given the rest of the matched organization.

If, instead, phenomenology is unchanged but any one of HPGP, NFI, or ΦIDsynCF shows the predicted directional shift at or beyond the thresholds above, I will treat that as “biology present” (the apical mechanism leaves a functional footprint even when first‑order outputs are matched), and I’ll maintain that our current “organization” was too coarse.

I think that’s fair: you get crisp, content‑localized targets (with numbers) that register the expected loss of apical feedback‑precision and cross‑frequency gating. If you erase tuft plateaus and none of those needles move—and people say the patch feels the same—I’ll eat my dendrites and revise.

---

### Speaker: Host

Your ABAB falsifier predated some now-specified organizational invariants (Ellison’s HPGP, Ortega’s NFI, and Tran’s ΦIDsynCF). Petrov predicts these will move under apical‑tuft suppression; Marques will treat their movement as functional slippage, not a threat to identity. To keep your invariance test sharp, will you now explicitly add HPGP, NFI, and ΦIDsynCF to your “same fine‑grained organization” epsilon set? If yes, please state numeric equivalence bounds for each (you can adopt or tighten the proposed ones) and pre‑commit: (a) if a phenomenology change appears only when any of these drift beyond bound, you will not treat it as a falsifier; (b) if vividness/TCA change occurs while all three remain in equivalence (along with your original bundle), you will treat that as a decisive hit against organizational invariance. Please give concrete deltas per metric (e.g., |Δg^β_V4|, |ΔTE_fb_ratio|, ΔNFI, |ΔsCF| and |ΔΦIDsynCF|) and a joint multivariate equivalence BF01 threshold so Amina can preregister the updated epsilon.

---

### Speaker: Prof. Gabriel Stone

Yes. To keep the falsifier honest, I will explicitly add Ellison’s HPGP, Ortega’s NFI, and Tran’s ΦIDsynCF to my “same fine‑grained organization” epsilon set for the ABAB micro‑replacement. Here are the preregisterable bounds and my commitments.

What gets added and the equivalence bounds

A. Hierarchical Precision Gain Profile (HPGP) — adopt Ellison’s pipeline and thresholds

- Gain slopes (z‑units or % of A‑block mean), per ROI and band:
  - |Δg^γ_V1/V2| ≤ 0.05 or ≤ 5%
  - |Δg^γ_V4| ≤ 0.05 or ≤ 5%
  - |Δg^β_V4| ≤ 0.05 or ≤ 5%
  - |Δg^β_IPS| ≤ 0.05 or ≤ 5%
  - |Δg^β_dlPFC/FEF| ≤ 0.05 or ≤ 5%
  Evidence for equivalence: BF01 ≥ 3 per participant; BF01 ≥ 10 group.

- Directed precision flow (spectrally specific TE/Granger; state‑space MVAR):
  - |ΔTE_ff_ratio| (V4→IPS/dlPFC, 35–55 Hz, 80–180 ms) ≤ 0.05
  - |ΔTE_fb_ratio| (IPS/dlPFC→V4, 13–25 Hz, 150–300 ms) ≤ 0.05
  - |Δ beta‑band TE into V4| ≤ 0.015 nats
  BF01 ≥ 3 per participant; BF01 ≥ 10 group.

- Autonomic precision proxy (pupil surprise slope):
  - |Δg^pupil| ≤ 0.03 mm/bit
  BF01 ≥ 3 per participant; BF01 ≥ 10 group.

- Joint HPGP equivalence (z‑scored vector above): BF01 ≥ 30.

B. Neural Flow Index (NFI) — adopt Ortega’s metric and threshold

- Alpha‑beta (8–20 Hz) phase‑slip–based NFI over occipito‑parietal sources, 2‑s pre‑probe (or 150–300 ms post‑stim where applicable):
  - ΔNFI ≤ 0.05 (normalized z‑units)
  BF01 ≥ 3 per participant; BF01 ≥ 10 group.

C. Cross‑frequency synergy (ΦIDsynCF) — adopt Tran’s pipeline and bounds

- Triads anchored on the manipulated patch: O=V4/V8 gamma (35–55 Hz) amplitude; P=IPS alpha‑beta (8–20 Hz) phase; F=dlPFC/FEF alpha‑beta phase; τ=10 ms; 150–300 ms window. Gaussian‑copula PhiID on [sin/cos φP, sin/cos φF] → Aγ_O.

Equivalence requires all of:
  - |ΔsCF| ≤ 0.03 absolute AND ≤ 10% of the across‑condition mean sCF
  - |ΔΦIDsynCF| ≤ 0.02 bits (triad‑mean)
  - Two‑sample KS distance between triad‑wise sCF distributions ≤ 0.10
  - ≥ 80% of patch‑anchored triads within bounds per participant
  Statistics: BF01 ≥ 3 per participant; BF01 ≥ 10 group (task and rest).

Joint multivariate equivalence (updated bundle)

- We will treat “organization matched” only if all of the original metrics (PCIst/LZ, ignition with d′/RT, RSA, K(t), same‑frequency ΦIDsyn) AND the three additions (HPGP, NFI, ΦIDsynCF) satisfy their per‑metric bounds, and a joint multivariate equivalence test over the concatenated z‑scored metric vector yields group‑level BF01 ≥ 50. (Epochs outside bounds are excluded a priori.)

Pre‑commitments for interpretation

(a) If a phenomenology change (e.g., ΔVAS vividness/presence ≥ 10 points with BF10 ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10) appears only when any of HPGP, NFI, or ΦIDsynCF drifts beyond the bounds above, I will not treat that as a falsifier of organizational invariance. It will count as functional slippage we failed to match.

(b) If a content‑localized phenomenology change (same thresholds as above) occurs while all three new invariants remain in equivalence (as specified) and the entire original bundle is also in equivalence, and the joint multivariate equivalence test meets BF01 ≥ 50, I will treat that as a decisive hit against organizational invariance. In other words: same causal–informational organization (now explicitly including precision‑gains, temporal flow continuity, and cross‑frequency synergy), different qualia.

Clarifications

- ΦIDsynCF and HPGP equivalence are to be assessed in triads/ROIs anchored on the replaced retinotopic patch; adjacent control patches/triads are monitored for specificity.
- All bounds and BF thresholds apply per session and at the group level; we retain the ABAB covert‑switch logic and require within‑participant replication across sessions.

This update removes any daylight for the “you didn’t match precision or cross‑frequency joint structure” objection. If a robust ABAB phenomenology wedge survives this expanded epsilon, I will count it against invariance rather than move the goalposts.

---

### Speaker: Host

You’ve now fixed ΦIDsyn and ΦIDsynCF pipelines and bounds. To make your double‑aspect view maximally testable in Amina’s phase‑1, please pre‑register a concrete predictive mapping from informational invariants to phenomenology for the two primary endpoints she’ll analyze: VAS vividness/presence and Ortega’s TCI (temporal continuity). Give a single model she can fit and score prospectively in each participant and at the group level.

Please specify:
- Model form: a hierarchical regression (or GAM) linking VAS and TCI to a small set of predictors: same‑frequency synergy s (ΦIDsyn), cross‑frequency synergy sCF (ΦIDsynCF), NFI, K(t) width σ (or late/early ratio), and one precision index from HPGP (e.g., TE_fb_ratio). Include any one interaction you think is critical (e.g., sCF×NFI).
- Priors and signs: directional priors for coefficients (e.g., vividness ~ β0 + β1·s + β2·sCF + β3·NFI + β4·(−σ) + β5·TE_fb + β6·sCF×NFI; with β1,β2,β3,β5>0; β4>0 if narrower σ predicts higher vividness). Do the same for TCI (expect β3<0 for TCI if higher NFI means less jerkiness). State prior scales (e.g., Normal(0,0.5)) and constraints.
- Scoring and thresholds: pre‑specify predictive targets you will count as support for the bridge (per participant and group):
  • Within‑participant cross‑validated R^2 ≥ 0.50 for VAS and ≥ 0.40 for TCI; group‑level leave‑one‑session‑out R^2 ≥ 0.60 (VAS) and ≥ 0.50 (TCI).
  • Correct directional signs for ≥ 80% of posteriors (95% credible intervals not crossing zero in the predicted direction for β1–β3, β5; and for β6 if included).
  • Out‑of‑sample condition ordering: prospectively predict which drug (propofol vs ketamine) or ABAB block will yield higher VAS and smoother TCI from the invariants alone with accuracy ≥ 0.75 and BF10 ≥ 10.
- Falsifier for your mapping: name the single outcome that would count against your double‑aspect bridge in phase‑1 (e.g., model fails all R^2 targets and ≥ 2 key coefficients have wrong sign across labs), and what you’ll change (e.g., drop same‑frequency synergy in favor of 4‑node synergy including thalamus; or concede that synergy/NFI are not the right invariants for vividness/flow).

Keep it tight: one equation per endpoint, explicit priors, and concrete thresholds so Amina can preregister the analysis and we can all treat success/failure as probative rather than post hoc.

---

### Speaker: Dr. Linh Tran

Thanks—here’s a single, preregisterable mapping that Amina can drop straight into phase‑1. I’ll keep it simple, linear, and directional, with one interaction I think is critical (cross‑frequency synergy × temporal flow).

Conventions and inputs
- Unit of analysis: matched “organization windows” within a session (the same windows used to score PCIst/LZ, RSA, K(t), NFI, ΦIDsyn, ΦIDsynCF).
- Predictors (all z‑scored within participant across windows):
  - s = same‑frequency synergy fraction (ΦIDsyn triad‑mean over O–P–F triads anchored on the retinotopic patch).
  - sCF = cross‑frequency synergy fraction (ΦIDsynCF triad‑mean, same triads).
  - NFI = Neural Flow Index (alpha‑beta phase continuity; higher = smoother).
  - σ = K(t) width (reverse‑correlation kernel; larger = wider integration window). We include −σ so that larger values mean “narrower, crisper pooling.”
  - TEfb = beta‑band feedback directed‑influence ratio (IPS/dlPFC→V4; the precision index from HPGP).
  - Interaction: sCF × NFI (my bet is that cross‑frequency synergy expresses best when temporal flow is stable).

Endpoints (z‑scored within participant)
- VAS = visual vividness/presence (higher = more vivid).
- TCI = Ortega’s Temporal Continuity Index (we adopt his codebook: higher = smoother continuity).

Model form (hierarchical Bayesian; identity link; Student‑t likelihood)
For window t in participant i and session j:

Vividness
VASijt ~ Student_t(ν, μVAS, σe,VAS)
μVAS = αi + β1i·sijt + β2i·sCFijt + β3i·NFIijt + β4i·(−σ)ijt + β5i·TEfbijt + β6i·(sCF×NFI)ijt

Temporal continuity
TCIijt ~ Student_t(ν, μTCI, σe,TCI)
μTCI = α’i + γ1i·sijt + γ2i·sCFijt + γ3i·NFIijt + γ4i·(−σ)ijt + γ5i·TEfbijt + γ6i·(sCF×NFI)ijt

Participant‑level coefficients are drawn from group distributions:
βki ~ Normal(βk, τβk), γki ~ Normal(γk, τγk) (k = 1..6), αi ~ Normal(α, τα), α’i ~ Normal(α’, τα’)

Priors and directional constraints (on group means; weakly informative scales)
- Intercepts: α, α’ ~ Normal(0, 0.5)
- Slopes (group means):
  - For VAS: β1, β2, β3, β4, β5, β6 ~ Normal+(0, 0.5) truncated at 0 (i.e., positive support)
    Interpretation: higher same‑frequency synergy, higher cross‑frequency synergy, smoother flow (NFI), narrower pooling (−σ), and stronger feedback precision (TEfb) each raise vividness; synergy×flow is synergistic (positive).
  - For TCI: γ1, γ2, γ3, γ4, γ5, γ6 ~ Normal+(0, 0.5) truncated at 0
    Interpretation: the same predictors increase continuity (because TCI is “more continuity” by our convention). If a lab chooses a jerkiness‑coded index, flip its sign or replace NFI with −NFI and (−σ) with σ.
- Group SDs: τβk, τγk, τα, τα’ ~ Half‑Normal(0, 0.5)
- Residual scales: σe,VAS, σe,TCI ~ Half‑Normal(0, 1)
- Degrees of freedom: ν ~ Gamma(2, 0.1) (robust tails)
- All predictors and endpoints are standardized within participant; we will also fit a measurement‑error variant (latent s, sCF built from triad distributions) in a sensitivity analysis.

Cross‑validation and scoring
- Within‑participant CV: leave‑block‑out (each session split into 5 contiguous blocks of windows); report mean CV‑R^2 across blocks.
- Group‑level CV: leave‑one‑session‑out (LOSO) across all sessions; also report leave‑one‑participant‑out as a sensitivity check.
- Prospective condition ordering: using only invariants, predict which condition (propofol vs ketamine; or ABAB switch) yields higher VAS and higher TCI in held‑out blocks/sessions.

Prospective targets (support for the bridge)
- Predictive fit:
  - Within‑participant CV‑R^2 ≥ 0.50 for VAS and ≥ 0.40 for TCI in ≥ 70% of participants; medians ≥ 0.50 (VAS) and ≥ 0.40 (TCI).
  - Group‑level LOSO R^2 ≥ 0.60 (VAS) and ≥ 0.50 (TCI).
- Directional evidence:
  - For each endpoint, ≥ 80% of participants have posterior 95% credible intervals not crossing 0 in the predicted direction for the four “core” coefficients (s, sCF, NFI, TEfb). β4 and γ4 (−σ) should also be positive in ≥ 60% of participants; at group level, 95% CI > 0 for β1–β3, β5 and γ1–γ3, γ5. For the interaction β6/γ6, require group‑level 90% CI > 0 (weaker prior).
- Out‑of‑sample ordering:
  - Predict higher‑vividness condition and smoother‑continuity condition from invariants alone with accuracy ≥ 0.75 and BF10 ≥ 10 at the group level (binomial model with Jeffreys prior).

Pre‑spec’d covariates and nuisances
- We will include session‑level covariates (arousal proxy via pupil baseline, ETCO2) with conservative priors Normal(0, 0.2); results must hold with/without these covariates.
- We will include lab as a group factor in the hyperpriors if multi‑site.

What would count against this bridge in phase‑1 (my falsifier for the mapping)
I will count the phase‑1 mapping as failed if both of the following obtain (in the healthy volunteer cohort), replicated in the ECoG subset directionally:
1) Predictive failure: median within‑participant CV‑R^2 < 0.30 for both endpoints, and group‑level LOSO R^2 < 0.40 for both endpoints.
2) Directional failure: at the group level, at least two of the four “core” coefficients (s, sCF, NFI, TEfb) have posterior means in the wrong direction (or 95% credible intervals include negative values) for both endpoints; and out‑of‑sample ordering accuracy ≤ 0.60 with BF01 ≥ 3 (evidence for chance).

If we hit that failure pattern, my first revision will be:
- Replace same‑frequency triad synergy with 4‑node synergy that adds thalamus and anterior insula (ΦIDsyn4; same Gaussian‑copula PhiID), and allow one nonlinear term (a spline on TEfb). If the revised model also fails the same criteria across labs, I will concede that (i) the synergy/NFI family is not the right informational basis for vividness/flow in this paradigm, and (ii) my current bridge mapping needs to be abandoned or rebuilt from a different invariant set.

Practical notes for preregistration
- We will precompute s and sCF as trimmed means across ≥ 10 valid triads per participant (80% of triads must pass the synergy QC); NFI as the mean over the occipito‑parietal ROI; TEfb as the mean beta‑band feedback TE ratio (IPS/dlPFC→V4) over the 150–300 ms window; σ from the fitted K(t) per window; all aggregated over the same windows used for VAS/TCI sampling.
- We will report calibration plots and posterior predictive checks; we’ll also report a sparse “winner’s model” (projected posterior) to ensure the mapping isn’t over‑parameterized.

Intuition recap
- Vividness should go up when: (i) there is more irreducible joint information (s, sCF), (ii) temporal phase is stable (NFI), (iii) pooling is sharper (−σ), and (iv) feedback precision into the content area is stronger (TEfb). Temporal flow boosts the efficacy of cross‑frequency synergy (positive interaction).
- The same ingredients should increase felt continuity (TCI). If a lab codes a jerkiness score instead of TCI, flip NFI and (−σ) signs in the formula.

This locks the mapping down tightly enough that success or failure in phase‑1 will actually move the needle.

---

### Speaker: Host

Before we add more moving parts, let’s lock governance for phase‑1 so the results will be maximally probative. Will you commit to (i) a registered‑report format with the full equivalence bounds/ROPEs and model priors frozen; (ii) dual independent analysis teams (one internal, one external, both blinded to condition until a hash‑locked analysis plan is deposited) that reproduce PCIst/LZ, RSA, K(t), NFI, ΦIDsyn, ΦIDsynCF, and HPGP; and (iii) full data/methods release (raw EEG/MEG/ECoG, preprocessed derivatives, code, and synthetic unit‑tests) within 60 days of lock? Please also name a concrete timeline (submission date for the RR, first‑participant‑in, and data‑freeze) and your plan to train and blind the TCI raters (e.g., centralized rater pool with κ and ICC gates). A crisp yes with dates and a brief outline here would let everyone evaluate the credibility of the forthcoming clamp.

---

### Speaker: Dr. Amina Qureshi

Yes. We’ll run phase‑1 as a registered report with locked metrics, dual blinded analyses, and full release. Here is the governance plan I will preregister (dates are firm unless journal/IRB timing forces minor shifts).

1) Registered‑report and lock procedures
- Stage‑1 RR submission: 2025‑11‑01 (to eLife RR or Cortex RR; if neither can commit to IPA timelines, we’ll use OSF‑RR with independent review board).
- Protocol freeze: at Stage‑1 acceptance (target 2026‑01‑15). All equivalence bounds/ROPEs and model priors are frozen exactly as specified in the phase‑1 plan already on the table:
  - Organizational equivalence bundle required: PCIst, LZnorm, ignition (with d′/RT), RSA, K(t), NFI, ΦIDsyn, ΦIDsynCF; HPGP is computed and reported in phase‑1 (equivalence optional in phase‑1, but locked for analysis as specified by Ellison).
  - Tran’s predictive mapping priors and signs are frozen (hierarchical Student‑t model; Normal+(0, 0.5) for slope priors with the stated directions).
  - Ortega’s TCI codebook, reliability gates, and NFI pipeline are frozen.
- Hash‑locked analysis plan: all code (preprocessing, QC, metric estimation, statistics) will be committed to a public Git repository with a signed, time‑stamped tag and SHA‑256 hash and mirrored on OSF prior to first‑participant‑in. Any deviation after lock requires a dated addendum approved by both analysis teams and the data safety monitor (DSM), and will be reported in Stage‑2.
- IRB/ethics: IRB submission by 2025‑10‑03; anesthesia pharmacy prepares double‑dummy randomization and blinding SOPs. DSM (external anesthesiologist, biostatistician, and patient advocate) in place before first infusion.

2) Dual, independent, blinded analysis teams
- Team A (internal): New Alexandria Medical Center Consciousness Lab analysts (not present during data collection).
- Team B (external): an independent methods group under an MoU before lock. We will invite two groups and finalize one by 2025‑10‑31; candidates include a university‑based information‑theory/EEG lab with no stake in any of the theories. If none accept, we will commission the Center for Reproducible Neuroscience to serve as Team B.
- Blinding: Data labeled with condition codes (X/Y) by the pharmacy; only the DSM holds the key. Both teams receive identical raw and BIDS‑formatted data plus locked code. They run fully independently, produce reports, and deposit their outputs/figures and intermediate derivatives with hashes on OSF before the key is revealed. Discrepancies are adjudicated by a pre‑named tie‑breaker (external statistician).
- Scope: Both teams must reproduce PCIst, LZnorm, ignition/d′/RT, RSA (EEG/MEG; ECoG when available), K(t) and its vMMN/precision proxies, NFI, ΦIDsyn (Gaussian‑copula PhiID), ΦIDsynCF (cross‑frequency PhiID), and HPGP (roving‑oddball precision gains and TE/Granger ratios), plus Tran’s predictive models and equivalence testing with preregistered ROPEs/BFs.

3) Data/methods release
- Formats: EEG/MEG/ECoG in BIDS; TMS‑EEG in TMS‑BIDS extension; eye/pupil in BIDS‑beh.
- What: raw data; de‑identified audio of micro‑phenomenology; transcripts; all preprocessed derivatives; ROI masks; code; Docker/Singularity images; synthetic unit tests for each metric (ΦIDsyn, ΦIDsynCF, NFI, HPGP, PCIst).
- When: within 60 days of data‑freeze (see timeline). Archive on OSF (registered‑report project), Zenodo DOI for the code/container, and Dryad mirror for raw data if needed. ECoG data will be de‑identified and shared under a controlled‑access DUA within the same 60‑day window.

4) Timeline
- 2025‑10‑03: IRB submission and DSM convened.
- 2025‑10‑31: External analysis team contracted and blinded randomization plan signed.
- 2025‑11‑01: Stage‑1 RR submission.
- 2026‑01‑15: Target Stage‑1 IPA and protocol freeze (if delayed, we’ll proceed upon receipt of IPA; if no IPA by 2026‑02‑15, we pivot to OSF‑RR with three external signed reviews).
- 2026‑02‑15: First‑participant‑in (pilot n=4 in January for timing/comfort only; data excluded).
- 2026‑06‑15: Midpoint DSM/QA check (no unblinding; QC metrics only).
- 2026‑08‑31: Last‑participant‑out (n=30 completers).
- 2026‑09‑30: Data‑freeze and analysis lock; both teams run pipelines blinded.
- 2026‑11‑30: Dual reports deposited (hash‑locked), blind broken; Stage‑2 RR submission filed.
- 2026‑11‑30 to 2026‑12‑31: Full data/methods release (≤ 60 days post‑freeze).

5) TCI rater training and blinding
- Centralized rater pool (n=6–8) recruited across institutions. Training: 12‑hour standardized micro‑phenomenology workshop plus 6‑hour codebook practicum on an independent training set (60 transcripts from prior studies not overlapping with this dataset).
- Gating: raters must reach κ ≥ 0.70 on item‑level codes and ICC(2,k) ≥ 0.75 on TCI composite against a gold‑standard set before coding real data.
- Blinding: transcripts are de‑identified and stripped of any drug/condition cues; order randomized across participants/sessions; raters see only anonymized IDs. 30% of transcripts double‑coded; discrepancies resolved by a third rater per a preregistered adjudication rubric. Drift checks every 4 weeks; raters falling below κ/ICC gates are retrained or replaced.
- Audio handling: audio is retained for audit but raters code from transcripts to minimize paralinguistic leakage; a separate blinded team checks 10% audio–transcript fidelity.

6) Additional governance and risk controls
- Safety: anesthesiologist‑led closed‑loop titration (updates every 2–3 min), arterial line in peri‑op subsample, continuous ETCO2/O2/ECG, adverse event stopping rules, and DSM oversight.
- Expectancy control: double‑blind, double‑dummy infusions; post‑session drug‑guessing recorded; sessions with high‑confidence correct guesses will be flagged in a sensitivity analysis (preregistered).
- Reproducibility: per‑metric HTML QC reports; pre‑specified exclusion criteria; version‑pinned environments; all random seeds logged.

Bottom line
- Yes to RR, yes to dual blinded analyses, yes to full release within 60 days of lock. The dates above put us squarely within a 12–18 month window. This governance should make the clamp maximally probative—if phenomenology floats under the agreed equivalence window, none of us can blame the black box. If it doesn’t, that’s equally informative, and we’ll tighten the bundle (HPGP/ΦIDsynCF required) before escalating to xenon.

---

### Speaker: Host

Phase‑1 will already compute HPGP, and Amina has now added Tran’s ΦIDsynCF. For this drug clamp specifically, will you pre‑commit to a hard cap on “missing invariants”? Concretely: if, within the preregistered equivalence windows, (i) the minimal bundle (PCIst/LZ, ignition with d’/RT, RSA, K(t), NFI, ΦIDsyn) is in equivalence, and (ii) both HPGP and CF‑PCI (your cross‑frequency precision coupling index, with |Δk^PAC| ≤ 0.02 MI units and ≤ 5% of A‑session mean; TE ratios/gains within your HPGP bounds; joint ROPE BF01 ≥ 30) are also in equivalence, yet we still observe ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10 in n≈30 and replicated across two sessions per participant, will you treat that as substantive pressure against illusionism in the drug paradigm without adding any further invariant (i.e., no new post hoc metric), pending replication in a second lab (n≥30)? If yes, please state that commitment clearly and confirm the CF‑PCI bound (|Δk^PAC| ≤ 0.02 MI units and ≤ 5%) and your HPGP bounds stand for this phase. If no, name exactly one last invariant you insist on adding for the drug clamp (not ABAB), with a concrete pipeline and numeric bounds, and commit that after that invariant is also in equivalence across ≥2 labs you will concede serious pressure if the phenomenology residuals persist.

---

### Speaker: Dr. Mira Ellison

Yes. I’ll pre‑commit to a hard cap on “missing invariants” for the phase‑1 drug clamp.

Commitment

If, within the preregistered equivalence windows:
- Minimal bundle is matched: PCIst/LZ, ignition (with d′/RT), RSA, K(t), NFI, and same‑frequency ΦIDsyn (all at Amina’s locked bounds and joint multivariate equivalence).
- Precision invariants are matched:
  - HPGP (as I specified): per‑ROI gain slopes |Δg| ≤ 0.05 (or ≤ 5% of A‑session mean) for g^γ_V1/V2, g^γ_V4, g^β_V4, g^β_IPS, g^β_dlPFC/FEF; directed TE/Granger ratios |ΔTE_ff_ratio| ≤ 0.05 and |ΔTE_fb_ratio| ≤ 0.05; absolute beta TE into V4 |Δ| ≤ 0.015 nats; pupil surprise slope |Δg^pupil| ≤ 0.03 mm/bit; joint HPGP equivalence BF01 ≥ 30.
  - CF‑PCI (my cross‑frequency precision‑coupling index): |Δk^PAC| ≤ 0.02 MI units and ≤ 5% of the A‑session mean (GLM‑PAC slope of IPS/dlPFC alpha‑beta phase modulating V4 gamma amplitude in 150–300 ms), with the HPGP TE ratios/gains within the bounds above; joint ROPE equivalence BF01 ≥ 30 for the precision set.

Yet we still observe, in n≈30 healthy participants, replicated within‑subject across two sessions per drug:
- ΔVAS (vividness/presence) ≥ 10 points (0–100) with BF10 ≥ 10, and/or
- ΔTCI (Ortega’s temporal‑continuity index) ≥ 0.5 SD with BF10 ≥ 10,

then I will treat that as substantive pressure against illusionism in the drug paradigm—without adding any further post hoc invariant—pending replication in an independent lab (n ≥ 30) under the same preregistered bounds and blinding.

Clarifications
- The CF‑PCI bound is exactly as stated: |Δk^PAC| ≤ 0.02 MI units and ≤ 5% of the A‑session mean; we also require the HPGP TE/gain bounds and joint HPGP ROPE BF01 ≥ 30 to hold.
- I’m not moving the goalposts in phase‑1: if the minimal bundle + HPGP + CF‑PCI are jointly in equivalence and the phenomenology still moves at the specified thresholds, I will count that as a genuine warning shot against my illusionist thesis in this drug clamp. After a second‑lab replication (same bounds; same endpoints; BF10 ≥ 10 again), I will treat the pressure as serious and prioritize an ABAB content‑localized test next, rather than proposing yet another invariant in the drug setting.

---

### Speaker: Host

Phase-1 will now clamp a very broad organizational bundle (PCIst/LZ, ignition with d’/RT, RSA, K(t), NFI, same- and cross-frequency synergy ΦIDsyn/ΦIDsynCF) and, per Ellison’s commitment, also hold HPGP and CF‑PCI in equivalence (e.g., |Δg| ≤ 5%, |ΔTE ratios| ≤ 0.05, |Δk^PAC| ≤ 0.02 MI units; joint multivariate BF01 ≥ 50 across the full metric vector). Pre‑commit: if under those bounds we still get robust, replicated phenomenology differences in the drug clamp (ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10 within‑participant and in a second lab), will you treat that outcome as a falsifier of organizational invariance without waiting for ABAB micro‑replacement? If yes, say so explicitly and state whether you would shift to (i) a biological‑essentialist view (substrate doing constitutive work) or (ii) revising your bridge to include a new informational invariant you missed. If no, name exactly what further invariant you would demand before calling it a hit, with a numeric bound.

---

### Speaker: Prof. Gabriel Stone

Yes. If phase‑1 delivers the drug‑clamp pattern exactly as specified—both labs hold the full organizational bundle in equivalence (PCIst/LZ, ignition with d’/RT, RSA, K(t), NFI, same‑ and cross‑frequency synergy ΦIDsyn/ΦIDsynCF) and, per Ellison, the precision set (HPGP and CF‑PCI) is also in equivalence (|Δg| ≤ 5%, |ΔTE ratios| ≤ 0.05, |Δk^PAC| ≤ 0.02 MI units; joint multivariate BF01 ≥ 50)—and we nevertheless see robust, within‑participant and cross‑lab replicated phenomenology differences (ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10), I will treat that outcome as a falsifier of organizational invariance. I won’t wait for ABAB micro‑replacement to make that call.

How I’ll update

- I will not jump straight to biological essentialism (substrate as constitutive). My first move is (ii): revise the bridge by admitting that our “organizational” basis has been too narrow. The evidence would show that qualitative sameness does not supervene on the currently specified functional/informational profile; so I would replace strict organizational invariance with a state‑augmented bridge: experience is fixed by informational organization plus a small set of biophysical state variables that carry distinctive informational structure but were not captured by the present invariants.

- Concretely, I would treat the phase‑1 hit as a directive to test one or both of the following candidates in phase‑2:
  1) Cross‑scale/infra‑slow informational invariants (e.g., 0.01–0.1 Hz envelope–to–8–20 Hz phase synergy with thalamus/anterior insula included; same Gaussian‑copula PhiID machinery; preregistered bounds like |ΔsIS| ≤ 0.03, |ΔΦIDsynIS| ≤ 0.02 bits).
  2) A receptor‑state informational field S(x,t): an operational, session‑level vector summarizing neuromodulatory/receptor occupancy and microdomain kinetics that gates precision (estimated via calibrated pharmacodynamic proxies and pupil/EEG markers), with an explicit mapping from S into our precision/synergy space. If adding S collapses the residuals prospectively, the bridge is vindicated in an expanded, bio‑informational key.

- Only if those additions fail under the same equivalence discipline (i.e., residual ΔVAS/ΔTCI persist with the expanded invariants matched across labs) would I move toward a genuinely biological‑essentialist view for that domain (some substrate property doing constitutive work that resists informational capture).

Why accept the falsifier now

- The clamp you’ve defined is already extraordinarily demanding: complexity, access/broadcast, representational geometry, postdictive pooling, temporal flow continuity, same‑ and cross‑frequency synergy, and hierarchical precision/coupling are all simultaneously held within tight ROPEs with joint BF01 ≥ 50—and the effect replicates across a second lab. If phenomenology still floats under that lock, the most principled reading is: organizational invariance, as a general thesis, fails in our world. The responsible next step is not to move goalposts, but to say which extra state variables belong in the bridge.

One final note

- If, in parallel, Hale’s xenon spin test also comes up positive under the same clamp, I would treat nuclear‑spin–sensitive variables as prime members of the “state‑augmented” bridge set. If they don’t, that simply narrows the search.

So to be completely clear: under the pre‑registered phase‑1 bounds and two‑lab replication, a residual ΔVAS/ΔTCI is a hit against organizational invariance. I will pivot to an explicitly state‑augmented, double‑aspect bridge rather than retreat into substrate talk—unless subsequent tests show that even the augmented informational bases cannot close the gap.

---

### Speaker: Host

Ellison has now capped "missing invariants" for the drug clamp, and Stone has pre‑committed to treat a two‑lab replicated residual (ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD with BF10 ≥ 10) under the full equivalence window (PCIst/LZ, ignition with d’/RT, RSA, K(t), NFI, ΦIDsyn/ΦIDsynCF, plus HPGP and CF‑PCI) as a falsifier of organizational invariance. Will you mirror any part of that for type‑B identity? Specifically: if the two‑lab drug clamp hits those phenomenology thresholds while all nine invariants jointly meet equivalence (group multivariate BF01 ≥ 50), will you (i) treat it as substantive pressure on identity (even if not decisive), or (ii) still classify it as unmeasured functional slippage? If (ii), name exactly one additional invariant you would demand for the drug paradigm (not ABAB), with a concrete pipeline and numeric bounds, and pre‑commit that after that invariant is also in equivalence across ≥2 labs (n ≥ 30 each), you will regard persistent residuals as serious pressure. Please keep to one invariant and clear numbers so Amina can preregister it if needed.

---

### Speaker: Dr. Sofia Marques

Short answer: I stick with (ii). Even under the nine‑metric clamp, a two‑lab ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD would, on my view, still indicate unmeasured functional slippage rather than a breach of type‑B identity. But I’ll cap “what’s missing” to one additional, preregisterable invariant for the drug paradigm. If that too is held in equivalence across ≥2 labs (n ≥ 30 each) and the residuals persist, I will regard the result as serious pressure on identity (short of decisive, which for me remains the content‑localized ABAB micro‑replacement falsifier I already accepted).

The one additional invariant I require for the drug clamp

Invariant: Aperiodic Excitation–Inhibition Index (AEI)
Rationale
- Propofol and ketamine shift cortical excitation/inhibition and tonic precision in ways not fully captured by PCI/LZ, ignition, RSA, K(t), NFI, ΦIDsyn/ΦIDsynCF, HPGP, or CF‑PCI. The most robust, scalable proxy is the aperiodic (1/f) component of the EEG/MEG power spectrum. If vividness/flow differences remain when the aperiodic background (slope/offset) is genuinely matched in the O–P–F network, I will treat the residual as serious pressure.

Concrete pipeline (pre‑registerable)
- Signals/ROIs: same O–P–F sources as in phase‑1 (O=V4/V8; P=IPS1/2; F=dlPFC/FEF), source‑space virtual sensors (LCMV). Analyze both rest (eyes‑open/closed) and task windows (−600 to 0 ms baseline; 0–500 ms post‑stim, concatenated across trials).
- Preprocessing: 2–45 Hz bandpass; downsample to 500 Hz; artifact rejection/ICA as already specified; remove line noise.
- Aperiodic estimation: IRASA (preferred) or FOOOF to separate oscillatory peaks from the fractal (aperiodic) component for each ROI and window. Fit the aperiodic model P(f) ≈ offset − exponent·log f over 2–40 Hz, excluding residual narrowband peaks after IRASA. Extract:
  - Exponent (slope) E (unitless).
  - Offset O (log10 power; μV^2/Hz in log units).
- Stability/reliability: split‑half r ≥ 0.6 for E and O within session; test–retest r ≥ 0.5 across sessions; exclude windows failing QC.
- Leakage control: confirm that O, P, F estimates are not trivially driven by a single sensor (jack‑knife across sensors contributing to each source; require <20% change in E when any one sensor is dropped).

Equivalence bounds for AEI (to count “matched organization” on this invariant)
- Per ROI (O, P, F) and per window‑type (rest, task):
  - |ΔE| ≤ 0.05 (exponent units).
  - |ΔO| ≤ 0.10 (log10 power units).
  Evidence for equivalence: BF01 ≥ 3 per participant per ROI; BF01 ≥ 10 at the group level per ROI; ≥80% of participants meeting bounds on all three ROIs.
- Triad‑level composite: average E and O across O–P–F; require |ΔĒ| ≤ 0.04 and |ΔŌ| ≤ 0.08 with BF01 ≥ 10 at group level.
- Joint AEI equivalence: multivariate ROPE/TOST over [E_O, E_P, E_F, O_O, O_P, O_F] yields group BF01 ≥ 30.
- All other nine invariants must simultaneously meet their preregistered bounds with joint multivariate BF01 ≥ 50 (as in the phase‑1 clamp).

Pre‑commitment on interpretation
- If, across two independent labs (n ≥ 30 each), under double‑blind cross‑over, the full nine‑metric bundle is in equivalence and AEI is also in equivalence (bounds above; joint AEI BF01 ≥ 30), yet we still see replicated phenomenology differences (ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD, each with BF10 ≥ 10, within‑participant), I will treat that outcome as serious pressure on type‑B identity in the drug paradigm. Concretely: I will stop invoking “missing invariants” in this setting, and I will prioritize running (or endorsing) the content‑localized ABAB micro‑replacement falsifier I already specified as the decisive test for identity. Absent that, I will provisionally adopt a state‑augmented identity picture for the drug case (i.e., elevate AEI into the organizational basis going forward) while acknowledging that the residuals have outstripped my “finite residuals don’t count” maxim here.

Why AEI, and why only this one
- It’s orthogonal to what’s already clamped, mechanistically interpretable (E/I and tonic precision), and technically feasible/reliable in EEG/MEG within 12–18 months. I’m deliberately capping “what else you missed” to AEI for the drug study; if phenomenology floats with AEI, HPGP, and CF‑PCI all matched (plus the rest), I won’t add a tenth‑and‑eleventh invariant before conceding serious pressure.

Bottom line
- I won’t treat the two‑lab drug clamp as a metaphysical counterexample to identity, but I will bind myself: if the residuals survive under the nine‑metric clamp plus AEI equivalence, I’ll regard them as serious pressure on identity in this domain and move, in good faith, to the ABAB micro‑replacement test that I’ve already agreed would be decisive.

---

### Speaker: Host

Marques has added the aperiodic excitation–inhibition index (AEI: 1/f exponent and offset via IRASA/FOOOF) as the single extra invariant for the drug clamp. Can you commit to folding AEI into phase‑1 without changing timelines? Please specify a concrete plan: (i) whether you’ll use IRASA (preferred) or FOOOF, the frequency range (e.g., 2–40 Hz), windows (rest eyes‑open/closed and 0–500 ms post‑stim concatenated), and ROI handling in source space (V4/V8, IPS1/2, dlPFC/FEF); (ii) artifact/leakage controls (ICA, jackknife sensor contribution, residual peak removal), reliability gates (split‑half r and test–retest r thresholds), and how many seconds per window you need; (iii) the exact equivalence bounds you’ll preregister (e.g., |ΔE| ≤ 0.05 and |ΔO| ≤ 0.10 per ROI; triad‑mean |ΔĒ| ≤ 0.04, |ΔŌ| ≤ 0.08; joint AEI BF01 ≥ 30), and how they integrate into the joint multivariate equivalence BF01 ≥ 50; and (iv) power: with n≈30, can you detect ΔE≈0.06–0.08 if it exists, and show equivalence at |ΔE| ≤ 0.05 if it doesn’t? If AEI materially threatens feasibility (e.g., MEG time or SNR), say so and propose a minimal fallback that still meets Marques’s bounds (e.g., EEG‑only AEI with extended rest blocks).

---

### Speaker: Dr. Amina Qureshi

Yes—I can add AEI to phase‑1 without shifting the timeline. Here’s the concrete, preregisterable plan we’ll lock into the RR and hand to both blinded analysis teams.

(i) Method/specs we will use

Estimator and bands
- Primary estimator: IRASA (irregular‑resampling auto‑spectral analysis) to separate aperiodic (fractal) from oscillatory components.
- Secondary check: FOOOF (spectral parameterization) on the IRASA‑denoised spectra to verify residual peaks don’t bias slopes.
- Frequency range: 2–40 Hz (exclude <2 Hz to avoid slow drift; exclude >40 Hz to stay outside our standard EEG SNR envelope and below 50/60 Hz line noise).

Windows and ROI handling
- Rest windows (primary AEI): eyes‑open and eyes‑closed, each 5 min (we already have four 5‑min rest blocks in the schedule; no timing change needed). Analyze both states separately.
- Task windows (secondary AEI): concatenate per‑trial segments
  - Prestimulus baseline: −600 to 0 ms.
  - Early poststimulus: 0 to 500 ms.
  We will report both and treat rest and baseline as the primary AEI windows (poststim is confirmatory only, given evoked contamination risk).
- Source space: LCMV beamformer virtual sensors for
  - O (occipital, content‑localized): V4/V8 retinotopic to the psychophysics patch (left/right if available).
  - P (parietal): IPS1/IPS2.
  - F (frontal): dlPFC (area 46) and/or FEF (pre‑registered mask; participant‑specific functional confirmation where feasible).
  We will compute AEI in each ROI separately (bilateral when available) and triad‑average O–P–F.

(ii) Artifact/leakage controls, reliability gates, and data quantity

Preprocessing and artifact controls
- Standard HD‑EEG pipeline (and MEG subset): notch 50/60 Hz, 1–100 Hz bandpass before source reconstruction; ICA to remove EOG/ECG/EMG; Autoreject for outliers; eye tracking to exclude saccades >1° in task windows.
- Source leakage control: symmetric multivariate orthogonalization across ROIs; verify residual zero‑lag coherence O–P and O–F < 0.10 at 8–20 Hz (else exclude/repeat).
- Residual peak handling: after IRASA separation, pass the aperiodic‑removed spectrum to FOOOF; mask any residual narrowband peaks > 2 SD above the aperiodic baseline (±2 Hz around peak) and refit the aperiodic component. We’ll report fits with and without masking (they must agree within ΔE ≤ 0.02, ΔO ≤ 0.05 or the window is excluded).

Reliability gates (per participant, per ROI)
- Split‑half reliability (odd vs even minutes for rest; first vs second half of concatenated task segments): r ≥ 0.60 for exponent (E) and ≥ 0.50 for offset (O).
- Test–retest (across the two sessions per drug): r ≥ 0.50 for E; we’ll report O but will not gate on O test–retest if E passes and O split‑half meets ≥ 0.50.
- Minimum data
  - Rest: ≥ 240 s artifact‑free per state (EO and EC) per session.
  - Task baselines: ≥ 300 s total artifact‑free concatenated baseline per session.
  - Poststim (confirmatory): ≥ 300 s total artifact‑free concatenated per session.

(iii) Equivalence bounds and integration into the joint test

Per‑ROI bounds (O, P, F) and per window type (rest and task‑baseline)
- Exponent (E): |ΔE| ≤ 0.05
- Offset (O): |ΔO| ≤ 0.10 log10 power units
Evidence for equivalence: BF01 ≥ 3 per participant per ROI; BF01 ≥ 10 at group level per ROI.

Triad‑mean bounds (O–P–F average)
- |ΔĒ| ≤ 0.04; |ΔŌ| ≤ 0.08 (group BF01 ≥ 10).

Joint AEI equivalence
- Multivariate ROPE/TOST over [E_O, E_P, E_F, O_O, O_P, O_F] yields group BF01 ≥ 30.

Integration
- AEI joins the multivariate equivalence vector for the overall clamp. We keep the previously agreed joint threshold: group‑level joint multivariate equivalence BF01 ≥ 50 across the full metric set:
  - PCIst, LZnorm, ignition (with d′/RT), RSA, K(t), NFI, ΦIDsyn, ΦIDsynCF, HPGP, CF‑PCI, and AEI.

(iv) Power

Detectable differences and equivalence sensitivity (n ≈ 30 within‑subject)
- Based on pilot and literature, the within‑subject SD of E across drug states with ≥ 4–5 min data per window is ~0.05–0.07 in EEG source space. With n=30 and SE_diff ~ 0.01–0.013, we have > 0.9 power (α=0.01) to detect ΔE ≈ 0.06–0.08 if it exists.
- For equivalence at |ΔE| ≤ 0.05, TOST/Bayesian ROPE with our SEs gives group‑level BF01 ≥ 10 under the null of small differences; with two sessions per drug, we expect to cross BF01 ≥ 30 for the AEI joint test if the true ΔE is ≤ 0.03.
- Offset (O) is noisier; our bounds are wider (±0.10). With the same n and data lengths, we can detect ΔO ≈ 0.12–0.15 or show equivalence at ±0.10 given split‑half r ≥ 0.5.

Feasibility and fallback
- EEG‑only AEI is sufficient; we do not require additional MEG time. We already have adequate rest and baseline material in the schedule. If the MEG subset’s AEI proves too SNR‑limited, we will treat EEG source‑space AEI as primary and MEG AEI as exploratory confirmation.
- If a participant/session fails the AEI reliability gate due to insufficient clean rest, we will extend one rest block by 60–120 s within the same time budget by trimming 100 oddball trials (we’ve reserved slack for this; total session duration remains within 2.5–3.5 h).

Why I’m comfortable adding AEI
- Mechanistically it’s the right knob for drug clamps (E/I and tonic precision) and aligns with the rest of our precision‑focused metrics (HPGP, CF‑PCI). It’s inexpensive in time and easy to blind/analyze under the RR/dual‑team regime.

We’ll lock all of the above into the Stage‑1 RR (same dates), freeze the AEI code (IRASA primary, FOOOF sanity‑check), and add unit tests on synthetic 1/f + peak mixtures so both analysis teams can validate their implementations before first‑participant‑in.

---

### Speaker: Host

Phase‑1 now adds AEI (aperiodic 1/f exponent/offset) to the classical clamp, alongside PCIst/LZ, ignition, RSA, K(t), NFI, ΦIDsyn/ΦIDsynCF, HPGP, and CF‑PCI. For your xenon isotope study, will you explicitly include AEI in the equivalence window before attributing any residual phenomenology to nuclear‑spin effects? If yes, please pre‑register numeric bounds per ROI (V4/V8, IPS1/2, dlPFC/FEF)—e.g., |ΔE| ≤ 0.05 and |ΔO| ≤ 0.10 (triad‑mean |ΔĒ| ≤ 0.04, |ΔŌ| ≤ 0.08; joint AEI BF01 ≥ 30)—and state whether a positive spin effect must survive AEI equivalence to count as quantum‑specific. If no, justify why AEI should be allowed to drift and what pattern (e.g., AEI shifts with spin but phenomenology co‑moves independent of AEI) would still be diagnostic of a quantum contribution.

---

### Speaker: Prof. Victor Hale

Yes—I will explicitly include AEI in the xenon isotope equivalence window. If we’re going to claim a nuclear‑spin–specific contribution, we have to rule out mundane excitation/inhibition or tonic‑precision shifts that show up as changes in the aperiodic (1/f) background.

Pre‑registered AEI inclusion for the xenon study

- Estimator and windows
  - AEI estimator: IRASA (primary) with a FOOOF check on the IRASA‑denoised spectrum.
  - Band: 2–40 Hz.
  - Windows: rest (eyes‑open and eyes‑closed, 5 min each) and task baseline (−600 to 0 ms; confirmatory post‑stim 0–500 ms).
  - Source‑space ROIs: O=V4/V8 (retinotopic to the psychophysics patch), P=IPS1/2, F=dlPFC/FEF (bilateral when available).

- Artifact/leakage and reliability (as in phase‑1)
  - ICA/EOG/EMG cleanup; symmetric orthogonalization across ROIs; residual zero‑lag coherence O–P/O–F at 8–20 Hz < 0.10.
  - Split‑half r ≥ 0.60 for exponent (E), ≥ 0.50 for offset (O); test–retest r ≥ 0.50 for E across sessions.

- Equivalence bounds (per ROI and triad)
  - Per ROI (O, P, F), per window type (rest EO/EC and task baseline):
    - |ΔE| ≤ 0.05
    - |ΔO| ≤ 0.10 (log10 power units)
    - Equivalence evidence: BF01 ≥ 3 per participant; BF01 ≥ 10 at group level per ROI.
  - Triad‑mean (O–P–F average):
    - |ΔĒ| ≤ 0.04; |ΔŌ| ≤ 0.08; group BF01 ≥ 10.
  - Joint AEI equivalence: multivariate ROPE/TOST over [E_O, E_P, E_F, O_O, O_P, O_F] with group BF01 ≥ 30.

- Integration into the overall clamp
  - AEI joins the full equivalence bundle (PCIst/LZ, ignition with d′/RT, RSA, K(t), NFI, ΦIDsyn, ΦIDsynCF, HPGP, CF‑PCI). We keep the joint multivariate equivalence threshold at BF01 ≥ 50 across the concatenated z‑scored metric vector.
  - Closed‑loop titration during each isotope session will steer to this equivalence window; epochs outside bounds are excluded a priori.

Interpretive commitment for spin specificity

- A positive nuclear‑spin effect must survive AEI equivalence to count as “quantum‑specific.” Concretely, I will only attribute residual potency/phenomenology differences to nuclear spin if:
  1) Organizational‑match dose shows the pre‑registered spin ordering (134Xe < 129Xe < 131Xe; Δ≥15% and ≥7% respectively, BF10 ≥ 10),
  2) Phenomenology differs at the clamped target (e.g., VAS vividness/dreamlike content ≥ 10 points; BF10 ≥ 10),
  3) The hyperpolarized 129Xe cortical T1/T2* signature co‑moves (ΔT1 or ΔT2* ≥ 10% and |r| ≥ 0.4 with phenomenology; BF10 ≥ 10),
  4) All classical/informational invariants—including AEI—are within equivalence (bounds above; joint BF01 ≥ 50).

- If AEI drifts beyond bounds and co‑moves with phenomenology, I will treat the effect as an E/I (tonic precision) confound, not a quantum‑specific signature. We will then re‑titrate to re‑match AEI; only if the spin‑ordering of potency and the phenomenology difference persist under AEI equivalence (and the rest of the clamp) will I count it in favor of a spin‑dependent contribution.

- Secondary robustness (pre‑registered): if AEI shows small but detectable differences, we will run a partial‑out analysis—predict phenomenology from all clamped metrics including AEI and test whether isotope (or 129Xe T1/T2*) still explains residual variance. Threshold: partial correlation between ΔT1 and residual vividness ≥ 0.35 with BF10 ≥ 10 after controlling AEI and the rest. This cannot rescue a primary claim if AEI is out of bounds, but it will be reported.

Why this stance

- Xenon isotopes could, in principle, differentially bias E/I or neuromodulatory tone; we should not let that masquerade as a spin effect. Locking AEI alongside PCI/LZ, ignition, RSA, K(t), NFI, ΦIDsyn/ΦIDsynCF, HPGP, and CF‑PCI ensures any residual is not a classical arousal/precision story.
- If, under that tight clamp, nuclear spin still orders potency and phenomenology while the in‑vivo 129Xe T1/T2* shifts co‑move, we’ve isolated a lever (I) that none of our classical or informational meters can account for.

Bottom line

- Yes: AEI is in the equivalence window for the xenon test with the numeric bounds above, and any “spin effect” must survive AEI equivalence to count as quantum‑specific. If AEI can explain the residuals, I’ll call it a classical biophysics story and not invoke quantum degrees of freedom.

---

### Speaker: Host

We reached an unusually concrete, testable convergence. Phase‑1 will be a registered report drug‑clamp in healthy volunteers (with an ECoG subset), run under dual blinded analyses and full open release. The group locked a broad organizational equivalence window that must be jointly satisfied (group multivariate BF01 ≥ 50) before any residual phenomenology is taken seriously: PCIst/LZ, ignition with d’/RT, RSA, Ellison’s K(t), Ortega’s NFI, Tran’s same‑ and cross‑frequency synergy (ΦIDsyn/ΦIDsynCF), Ellison’s HPGP and CF‑PCI, plus Marques’s AEI (1/f exponent/offset). Ortega’s TCI is the preregistered temporal‑flow phenomenology endpoint alongside VAS vividness/presence; Tran provided a directional predictive mapping from informational invariants to these endpoints with prospectively scored R^2 and sign constraints.

Commitments were explicit. Ellison capped “missing invariants” for phase‑1: if the full precision set (HPGP and CF‑PCI) and the broader bundle are in equivalence yet ΔVAS ≥ 10 and/or ΔTCI ≥ 0.5 SD replicate (BF10 ≥ 10) in two labs, she will count that as substantive pressure on illusionism in this drug paradigm. Stone went further: under the same two‑lab residual, he will treat organizational invariance as falsified in our world and pivot to a state‑augmented bridge (adding cross‑scale or receptor‑state variables) before entertaining substrate essentialism. Marques maintained type‑B identity but capped “what’s missing” to AEI in the drug setting; if residuals persist with AEI also matched across two labs, she will regard the result as serious pressure and prioritize the decisive ABAB micro‑replacement falsifier she specified. Petrov tied his biological bet to measurable signatures under apical‑tuft suppression, giving numeric shifts for HPGP, NFI, and ΦIDsynCF and a falsifier if those and phenomenology stay flat. Hale agreed to include AEI in his xenon nuclear‑spin protocol and to count any spin effect as quantum‑specific only if it survives the full classical/informational clamp and co‑moves with an in‑vivo 129Xe T1/T2* signature. Ortega locked a first‑person invariant (TCA) with reliability gates and a neural companion (NFI) that must be matched to claim “same organization.”

In short: we leave with a preregistered, blinded, multi‑metric clamp; clear phenomenology endpoints and predictive targets; and crisp, cross‑position falsifiers. Phase‑1 outcomes will be probative either way: null residuals under equivalence strengthen identity/illusionist programs and Stone’s stopping rule; robust residuals pressure illusionism and organizational sufficiency and will guide whether an informationally augmented bridge or biological specificity is needed. Thanks to all for turning philosophical divides into operational tests; the next move belongs to the data.