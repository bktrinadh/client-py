#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_name, jsondict, strict=True):
        """ Instantiate a resource of the type correlating to "resource_name".
        
        :param str resource_name: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_name:
            from . import account
            return account.Account(jsondict, strict=strict)
        if "Address" == resource_name:
            from . import address
            return address.Address(jsondict, strict=strict)
        if "Age" == resource_name:
            from . import age
            return age.Age(jsondict, strict=strict)
        if "AllergyIntolerance" == resource_name:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict, strict=strict)
        if "AllergyIntoleranceReaction" == resource_name:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntoleranceReaction(jsondict, strict=strict)
        if "Annotation" == resource_name:
            from . import annotation
            return annotation.Annotation(jsondict, strict=strict)
        if "Appointment" == resource_name:
            from . import appointment
            return appointment.Appointment(jsondict, strict=strict)
        if "AppointmentParticipant" == resource_name:
            from . import appointment
            return appointment.AppointmentParticipant(jsondict, strict=strict)
        if "AppointmentResponse" == resource_name:
            from . import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict, strict=strict)
        if "Attachment" == resource_name:
            from . import attachment
            return attachment.Attachment(jsondict, strict=strict)
        if "AuditEvent" == resource_name:
            from . import auditevent
            return auditevent.AuditEvent(jsondict, strict=strict)
        if "AuditEventEvent" == resource_name:
            from . import auditevent
            return auditevent.AuditEventEvent(jsondict, strict=strict)
        if "AuditEventObject" == resource_name:
            from . import auditevent
            return auditevent.AuditEventObject(jsondict, strict=strict)
        if "AuditEventObjectDetail" == resource_name:
            from . import auditevent
            return auditevent.AuditEventObjectDetail(jsondict, strict=strict)
        if "AuditEventParticipant" == resource_name:
            from . import auditevent
            return auditevent.AuditEventParticipant(jsondict, strict=strict)
        if "AuditEventParticipantNetwork" == resource_name:
            from . import auditevent
            return auditevent.AuditEventParticipantNetwork(jsondict, strict=strict)
        if "AuditEventSource" == resource_name:
            from . import auditevent
            return auditevent.AuditEventSource(jsondict, strict=strict)
        if "BackboneElement" == resource_name:
            from . import backboneelement
            return backboneelement.BackboneElement(jsondict, strict=strict)
        if "Basic" == resource_name:
            from . import basic
            return basic.Basic(jsondict, strict=strict)
        if "Binary" == resource_name:
            from . import binary
            return binary.Binary(jsondict, strict=strict)
        if "BodySite" == resource_name:
            from . import bodysite
            return bodysite.BodySite(jsondict, strict=strict)
        if "Bundle" == resource_name:
            from . import bundle
            return bundle.Bundle(jsondict, strict=strict)
        if "BundleEntry" == resource_name:
            from . import bundle
            return bundle.BundleEntry(jsondict, strict=strict)
        if "BundleEntryRequest" == resource_name:
            from . import bundle
            return bundle.BundleEntryRequest(jsondict, strict=strict)
        if "BundleEntryResponse" == resource_name:
            from . import bundle
            return bundle.BundleEntryResponse(jsondict, strict=strict)
        if "BundleEntrySearch" == resource_name:
            from . import bundle
            return bundle.BundleEntrySearch(jsondict, strict=strict)
        if "BundleLink" == resource_name:
            from . import bundle
            return bundle.BundleLink(jsondict, strict=strict)
        if "CarePlan" == resource_name:
            from . import careplan
            return careplan.CarePlan(jsondict, strict=strict)
        if "CarePlanActivity" == resource_name:
            from . import careplan
            return careplan.CarePlanActivity(jsondict, strict=strict)
        if "CarePlanActivityDetail" == resource_name:
            from . import careplan
            return careplan.CarePlanActivityDetail(jsondict, strict=strict)
        if "CarePlanParticipant" == resource_name:
            from . import careplan
            return careplan.CarePlanParticipant(jsondict, strict=strict)
        if "CarePlanRelatedPlan" == resource_name:
            from . import careplan
            return careplan.CarePlanRelatedPlan(jsondict, strict=strict)
        if "Claim" == resource_name:
            from . import claim
            return claim.Claim(jsondict, strict=strict)
        if "ClaimCoverage" == resource_name:
            from . import claim
            return claim.ClaimCoverage(jsondict, strict=strict)
        if "ClaimDiagnosis" == resource_name:
            from . import claim
            return claim.ClaimDiagnosis(jsondict, strict=strict)
        if "ClaimItem" == resource_name:
            from . import claim
            return claim.ClaimItem(jsondict, strict=strict)
        if "ClaimItemDetail" == resource_name:
            from . import claim
            return claim.ClaimItemDetail(jsondict, strict=strict)
        if "ClaimItemDetailSubDetail" == resource_name:
            from . import claim
            return claim.ClaimItemDetailSubDetail(jsondict, strict=strict)
        if "ClaimItemProsthesis" == resource_name:
            from . import claim
            return claim.ClaimItemProsthesis(jsondict, strict=strict)
        if "ClaimMissingTeeth" == resource_name:
            from . import claim
            return claim.ClaimMissingTeeth(jsondict, strict=strict)
        if "ClaimPayee" == resource_name:
            from . import claim
            return claim.ClaimPayee(jsondict, strict=strict)
        if "ClaimResponse" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponse(jsondict, strict=strict)
        if "ClaimResponseAddItem" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict, strict=strict)
        if "ClaimResponseAddItemAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemAdjudication(jsondict, strict=strict)
        if "ClaimResponseAddItemDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict, strict=strict)
        if "ClaimResponseAddItemDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetailAdjudication(jsondict, strict=strict)
        if "ClaimResponseCoverage" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseCoverage(jsondict, strict=strict)
        if "ClaimResponseError" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseError(jsondict, strict=strict)
        if "ClaimResponseItem" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItem(jsondict, strict=strict)
        if "ClaimResponseItemAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict, strict=strict)
        if "ClaimResponseItemDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict, strict=strict)
        if "ClaimResponseItemDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailAdjudication(jsondict, strict=strict)
        if "ClaimResponseItemDetailSubDetail" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict, strict=strict)
        if "ClaimResponseItemDetailSubDetailAdjudication" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetailAdjudication(jsondict, strict=strict)
        if "ClaimResponseNote" == resource_name:
            from . import claimresponse
            return claimresponse.ClaimResponseNote(jsondict, strict=strict)
        if "ClinicalImpression" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict, strict=strict)
        if "ClinicalImpressionFinding" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict, strict=strict)
        if "ClinicalImpressionInvestigations" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionInvestigations(jsondict, strict=strict)
        if "ClinicalImpressionRuledOut" == resource_name:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionRuledOut(jsondict, strict=strict)
        if "CodeableConcept" == resource_name:
            from . import codeableconcept
            return codeableconcept.CodeableConcept(jsondict, strict=strict)
        if "Coding" == resource_name:
            from . import coding
            return coding.Coding(jsondict, strict=strict)
        if "Communication" == resource_name:
            from . import communication
            return communication.Communication(jsondict, strict=strict)
        if "CommunicationPayload" == resource_name:
            from . import communication
            return communication.CommunicationPayload(jsondict, strict=strict)
        if "CommunicationRequest" == resource_name:
            from . import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict, strict=strict)
        if "CommunicationRequestPayload" == resource_name:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict, strict=strict)
        if "Composition" == resource_name:
            from . import composition
            return composition.Composition(jsondict, strict=strict)
        if "CompositionAttester" == resource_name:
            from . import composition
            return composition.CompositionAttester(jsondict, strict=strict)
        if "CompositionEvent" == resource_name:
            from . import composition
            return composition.CompositionEvent(jsondict, strict=strict)
        if "CompositionSection" == resource_name:
            from . import composition
            return composition.CompositionSection(jsondict, strict=strict)
        if "ConceptMap" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMap(jsondict, strict=strict)
        if "ConceptMapContact" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapContact(jsondict, strict=strict)
        if "ConceptMapElement" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElement(jsondict, strict=strict)
        if "ConceptMapElementTarget" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElementTarget(jsondict, strict=strict)
        if "ConceptMapElementTargetDependsOn" == resource_name:
            from . import conceptmap
            return conceptmap.ConceptMapElementTargetDependsOn(jsondict, strict=strict)
        if "Condition" == resource_name:
            from . import condition
            return condition.Condition(jsondict, strict=strict)
        if "ConditionEvidence" == resource_name:
            from . import condition
            return condition.ConditionEvidence(jsondict, strict=strict)
        if "ConditionStage" == resource_name:
            from . import condition
            return condition.ConditionStage(jsondict, strict=strict)
        if "Conformance" == resource_name:
            from . import conformance
            return conformance.Conformance(jsondict, strict=strict)
        if "ConformanceContact" == resource_name:
            from . import conformance
            return conformance.ConformanceContact(jsondict, strict=strict)
        if "ConformanceDocument" == resource_name:
            from . import conformance
            return conformance.ConformanceDocument(jsondict, strict=strict)
        if "ConformanceImplementation" == resource_name:
            from . import conformance
            return conformance.ConformanceImplementation(jsondict, strict=strict)
        if "ConformanceMessaging" == resource_name:
            from . import conformance
            return conformance.ConformanceMessaging(jsondict, strict=strict)
        if "ConformanceMessagingEndpoint" == resource_name:
            from . import conformance
            return conformance.ConformanceMessagingEndpoint(jsondict, strict=strict)
        if "ConformanceMessagingEvent" == resource_name:
            from . import conformance
            return conformance.ConformanceMessagingEvent(jsondict, strict=strict)
        if "ConformanceRest" == resource_name:
            from . import conformance
            return conformance.ConformanceRest(jsondict, strict=strict)
        if "ConformanceRestInteraction" == resource_name:
            from . import conformance
            return conformance.ConformanceRestInteraction(jsondict, strict=strict)
        if "ConformanceRestOperation" == resource_name:
            from . import conformance
            return conformance.ConformanceRestOperation(jsondict, strict=strict)
        if "ConformanceRestResource" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResource(jsondict, strict=strict)
        if "ConformanceRestResourceInteraction" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResourceInteraction(jsondict, strict=strict)
        if "ConformanceRestResourceSearchParam" == resource_name:
            from . import conformance
            return conformance.ConformanceRestResourceSearchParam(jsondict, strict=strict)
        if "ConformanceRestSecurity" == resource_name:
            from . import conformance
            return conformance.ConformanceRestSecurity(jsondict, strict=strict)
        if "ConformanceRestSecurityCertificate" == resource_name:
            from . import conformance
            return conformance.ConformanceRestSecurityCertificate(jsondict, strict=strict)
        if "ConformanceSoftware" == resource_name:
            from . import conformance
            return conformance.ConformanceSoftware(jsondict, strict=strict)
        if "ContactPoint" == resource_name:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict, strict=strict)
        if "Contract" == resource_name:
            from . import contract
            return contract.Contract(jsondict, strict=strict)
        if "ContractActor" == resource_name:
            from . import contract
            return contract.ContractActor(jsondict, strict=strict)
        if "ContractFriendly" == resource_name:
            from . import contract
            return contract.ContractFriendly(jsondict, strict=strict)
        if "ContractLegal" == resource_name:
            from . import contract
            return contract.ContractLegal(jsondict, strict=strict)
        if "ContractRule" == resource_name:
            from . import contract
            return contract.ContractRule(jsondict, strict=strict)
        if "ContractSigner" == resource_name:
            from . import contract
            return contract.ContractSigner(jsondict, strict=strict)
        if "ContractTerm" == resource_name:
            from . import contract
            return contract.ContractTerm(jsondict, strict=strict)
        if "ContractTermActor" == resource_name:
            from . import contract
            return contract.ContractTermActor(jsondict, strict=strict)
        if "ContractTermValuedItem" == resource_name:
            from . import contract
            return contract.ContractTermValuedItem(jsondict, strict=strict)
        if "ContractValuedItem" == resource_name:
            from . import contract
            return contract.ContractValuedItem(jsondict, strict=strict)
        if "Count" == resource_name:
            from . import count
            return count.Count(jsondict, strict=strict)
        if "Coverage" == resource_name:
            from . import coverage
            return coverage.Coverage(jsondict, strict=strict)
        if "DataElement" == resource_name:
            from . import dataelement
            return dataelement.DataElement(jsondict, strict=strict)
        if "DataElementContact" == resource_name:
            from . import dataelement
            return dataelement.DataElementContact(jsondict, strict=strict)
        if "DataElementMapping" == resource_name:
            from . import dataelement
            return dataelement.DataElementMapping(jsondict, strict=strict)
        if "DetectedIssue" == resource_name:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict, strict=strict)
        if "DetectedIssueMitigation" == resource_name:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict, strict=strict)
        if "Device" == resource_name:
            from . import device
            return device.Device(jsondict, strict=strict)
        if "DeviceComponent" == resource_name:
            from . import devicecomponent
            return devicecomponent.DeviceComponent(jsondict, strict=strict)
        if "DeviceComponentProductionSpecification" == resource_name:
            from . import devicecomponent
            return devicecomponent.DeviceComponentProductionSpecification(jsondict, strict=strict)
        if "DeviceMetric" == resource_name:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict, strict=strict)
        if "DeviceMetricCalibration" == resource_name:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict, strict=strict)
        if "DeviceUseRequest" == resource_name:
            from . import deviceuserequest
            return deviceuserequest.DeviceUseRequest(jsondict, strict=strict)
        if "DeviceUseStatement" == resource_name:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict, strict=strict)
        if "DiagnosticOrder" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrder(jsondict, strict=strict)
        if "DiagnosticOrderEvent" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrderEvent(jsondict, strict=strict)
        if "DiagnosticOrderItem" == resource_name:
            from . import diagnosticorder
            return diagnosticorder.DiagnosticOrderItem(jsondict, strict=strict)
        if "DiagnosticReport" == resource_name:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict, strict=strict)
        if "DiagnosticReportImage" == resource_name:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportImage(jsondict, strict=strict)
        if "Distance" == resource_name:
            from . import distance
            return distance.Distance(jsondict, strict=strict)
        if "DocumentManifest" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict, strict=strict)
        if "DocumentManifestContent" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifestContent(jsondict, strict=strict)
        if "DocumentManifestRelated" == resource_name:
            from . import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict, strict=strict)
        if "DocumentReference" == resource_name:
            from . import documentreference
            return documentreference.DocumentReference(jsondict, strict=strict)
        if "DocumentReferenceContent" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContent(jsondict, strict=strict)
        if "DocumentReferenceContext" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContext(jsondict, strict=strict)
        if "DocumentReferenceContextRelated" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceContextRelated(jsondict, strict=strict)
        if "DocumentReferenceRelatesTo" == resource_name:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict, strict=strict)
        if "DomainResource" == resource_name:
            from . import domainresource
            return domainresource.DomainResource(jsondict, strict=strict)
        if "Duration" == resource_name:
            from . import duration
            return duration.Duration(jsondict, strict=strict)
        if "Element" == resource_name:
            from . import element
            return element.Element(jsondict, strict=strict)
        if "ElementDefinition" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinition(jsondict, strict=strict)
        if "ElementDefinitionBase" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBase(jsondict, strict=strict)
        if "ElementDefinitionBinding" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict, strict=strict)
        if "ElementDefinitionConstraint" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict, strict=strict)
        if "ElementDefinitionMapping" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict, strict=strict)
        if "ElementDefinitionSlicing" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict, strict=strict)
        if "ElementDefinitionType" == resource_name:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict, strict=strict)
        if "EligibilityRequest" == resource_name:
            from . import eligibilityrequest
            return eligibilityrequest.EligibilityRequest(jsondict, strict=strict)
        if "EligibilityResponse" == resource_name:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponse(jsondict, strict=strict)
        if "Encounter" == resource_name:
            from . import encounter
            return encounter.Encounter(jsondict, strict=strict)
        if "EncounterHospitalization" == resource_name:
            from . import encounter
            return encounter.EncounterHospitalization(jsondict, strict=strict)
        if "EncounterLocation" == resource_name:
            from . import encounter
            return encounter.EncounterLocation(jsondict, strict=strict)
        if "EncounterParticipant" == resource_name:
            from . import encounter
            return encounter.EncounterParticipant(jsondict, strict=strict)
        if "EncounterStatusHistory" == resource_name:
            from . import encounter
            return encounter.EncounterStatusHistory(jsondict, strict=strict)
        if "EnrollmentRequest" == resource_name:
            from . import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict, strict=strict)
        if "EnrollmentResponse" == resource_name:
            from . import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict, strict=strict)
        if "EpisodeOfCare" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict, strict=strict)
        if "EpisodeOfCareCareTeam" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareCareTeam(jsondict, strict=strict)
        if "EpisodeOfCareStatusHistory" == resource_name:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict, strict=strict)
        if "ExplanationOfBenefit" == resource_name:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict, strict=strict)
        if "Extension" == resource_name:
            from . import extension
            return extension.Extension(jsondict, strict=strict)
        if "FamilyMemberHistory" == resource_name:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict, strict=strict)
        if "FamilyMemberHistoryCondition" == resource_name:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict, strict=strict)
        if "Flag" == resource_name:
            from . import flag
            return flag.Flag(jsondict, strict=strict)
        if "Goal" == resource_name:
            from . import goal
            return goal.Goal(jsondict, strict=strict)
        if "GoalOutcome" == resource_name:
            from . import goal
            return goal.GoalOutcome(jsondict, strict=strict)
        if "Group" == resource_name:
            from . import group
            return group.Group(jsondict, strict=strict)
        if "GroupCharacteristic" == resource_name:
            from . import group
            return group.GroupCharacteristic(jsondict, strict=strict)
        if "GroupMember" == resource_name:
            from . import group
            return group.GroupMember(jsondict, strict=strict)
        if "HealthcareService" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareService(jsondict, strict=strict)
        if "HealthcareServiceAvailableTime" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict, strict=strict)
        if "HealthcareServiceNotAvailable" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict, strict=strict)
        if "HealthcareServiceServiceType" == resource_name:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceServiceType(jsondict, strict=strict)
        if "HumanName" == resource_name:
            from . import humanname
            return humanname.HumanName(jsondict, strict=strict)
        if "Identifier" == resource_name:
            from . import identifier
            return identifier.Identifier(jsondict, strict=strict)
        if "ImagingObjectSelection" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelection(jsondict, strict=strict)
        if "ImagingObjectSelectionStudy" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudy(jsondict, strict=strict)
        if "ImagingObjectSelectionStudySeries" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeries(jsondict, strict=strict)
        if "ImagingObjectSelectionStudySeriesInstance" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstance(jsondict, strict=strict)
        if "ImagingObjectSelectionStudySeriesInstanceFrames" == resource_name:
            from . import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstanceFrames(jsondict, strict=strict)
        if "ImagingStudy" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict, strict=strict)
        if "ImagingStudySeries" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict, strict=strict)
        if "ImagingStudySeriesInstance" == resource_name:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict, strict=strict)
        if "Immunization" == resource_name:
            from . import immunization
            return immunization.Immunization(jsondict, strict=strict)
        if "ImmunizationExplanation" == resource_name:
            from . import immunization
            return immunization.ImmunizationExplanation(jsondict, strict=strict)
        if "ImmunizationReaction" == resource_name:
            from . import immunization
            return immunization.ImmunizationReaction(jsondict, strict=strict)
        if "ImmunizationRecommendation" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict, strict=strict)
        if "ImmunizationRecommendationRecommendation" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict, strict=strict)
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict, strict=strict)
        if "ImmunizationRecommendationRecommendationProtocol" == resource_name:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(jsondict, strict=strict)
        if "ImmunizationVaccinationProtocol" == resource_name:
            from . import immunization
            return immunization.ImmunizationVaccinationProtocol(jsondict, strict=strict)
        if "ImplementationGuide" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict, strict=strict)
        if "ImplementationGuideContact" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideContact(jsondict, strict=strict)
        if "ImplementationGuideDependency" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependency(jsondict, strict=strict)
        if "ImplementationGuideGlobal" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict, strict=strict)
        if "ImplementationGuidePackage" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackage(jsondict, strict=strict)
        if "ImplementationGuidePackageResource" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackageResource(jsondict, strict=strict)
        if "ImplementationGuidePage" == resource_name:
            from . import implementationguide
            return implementationguide.ImplementationGuidePage(jsondict, strict=strict)
        if "List" == resource_name:
            from . import list
            return list.List(jsondict, strict=strict)
        if "ListEntry" == resource_name:
            from . import list
            return list.ListEntry(jsondict, strict=strict)
        if "Location" == resource_name:
            from . import location
            return location.Location(jsondict, strict=strict)
        if "LocationPosition" == resource_name:
            from . import location
            return location.LocationPosition(jsondict, strict=strict)
        if "Media" == resource_name:
            from . import media
            return media.Media(jsondict, strict=strict)
        if "Medication" == resource_name:
            from . import medication
            return medication.Medication(jsondict, strict=strict)
        if "MedicationAdministration" == resource_name:
            from . import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict, strict=strict)
        if "MedicationAdministrationDosage" == resource_name:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict, strict=strict)
        if "MedicationDispense" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispense(jsondict, strict=strict)
        if "MedicationDispenseDosageInstruction" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseDosageInstruction(jsondict, strict=strict)
        if "MedicationDispenseSubstitution" == resource_name:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict, strict=strict)
        if "MedicationOrder" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrder(jsondict, strict=strict)
        if "MedicationOrderDispenseRequest" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderDispenseRequest(jsondict, strict=strict)
        if "MedicationOrderDosageInstruction" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderDosageInstruction(jsondict, strict=strict)
        if "MedicationOrderSubstitution" == resource_name:
            from . import medicationorder
            return medicationorder.MedicationOrderSubstitution(jsondict, strict=strict)
        if "MedicationPackage" == resource_name:
            from . import medication
            return medication.MedicationPackage(jsondict, strict=strict)
        if "MedicationPackageContent" == resource_name:
            from . import medication
            return medication.MedicationPackageContent(jsondict, strict=strict)
        if "MedicationProduct" == resource_name:
            from . import medication
            return medication.MedicationProduct(jsondict, strict=strict)
        if "MedicationProductBatch" == resource_name:
            from . import medication
            return medication.MedicationProductBatch(jsondict, strict=strict)
        if "MedicationProductIngredient" == resource_name:
            from . import medication
            return medication.MedicationProductIngredient(jsondict, strict=strict)
        if "MedicationStatement" == resource_name:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict, strict=strict)
        if "MedicationStatementDosage" == resource_name:
            from . import medicationstatement
            return medicationstatement.MedicationStatementDosage(jsondict, strict=strict)
        if "MessageHeader" == resource_name:
            from . import messageheader
            return messageheader.MessageHeader(jsondict, strict=strict)
        if "MessageHeaderDestination" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderDestination(jsondict, strict=strict)
        if "MessageHeaderResponse" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderResponse(jsondict, strict=strict)
        if "MessageHeaderSource" == resource_name:
            from . import messageheader
            return messageheader.MessageHeaderSource(jsondict, strict=strict)
        if "Meta" == resource_name:
            from . import meta
            return meta.Meta(jsondict, strict=strict)
        if "Money" == resource_name:
            from . import money
            return money.Money(jsondict, strict=strict)
        if "NamingSystem" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystem(jsondict, strict=strict)
        if "NamingSystemContact" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystemContact(jsondict, strict=strict)
        if "NamingSystemUniqueId" == resource_name:
            from . import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict, strict=strict)
        if "Narrative" == resource_name:
            from . import narrative
            return narrative.Narrative(jsondict, strict=strict)
        if "NutritionOrder" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrder(jsondict, strict=strict)
        if "NutritionOrderEnteralFormula" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict, strict=strict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormulaAdministration(jsondict, strict=strict)
        if "NutritionOrderOralDiet" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict, strict=strict)
        if "NutritionOrderOralDietNutrient" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict, strict=strict)
        if "NutritionOrderOralDietTexture" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict, strict=strict)
        if "NutritionOrderSupplement" == resource_name:
            from . import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict, strict=strict)
        if "Observation" == resource_name:
            from . import observation
            return observation.Observation(jsondict, strict=strict)
        if "ObservationComponent" == resource_name:
            from . import observation
            return observation.ObservationComponent(jsondict, strict=strict)
        if "ObservationReferenceRange" == resource_name:
            from . import observation
            return observation.ObservationReferenceRange(jsondict, strict=strict)
        if "ObservationRelated" == resource_name:
            from . import observation
            return observation.ObservationRelated(jsondict, strict=strict)
        if "OperationDefinition" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinition(jsondict, strict=strict)
        if "OperationDefinitionContact" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionContact(jsondict, strict=strict)
        if "OperationDefinitionParameter" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict, strict=strict)
        if "OperationDefinitionParameterBinding" == resource_name:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterBinding(jsondict, strict=strict)
        if "OperationOutcome" == resource_name:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict, strict=strict)
        if "OperationOutcomeIssue" == resource_name:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict, strict=strict)
        if "Order" == resource_name:
            from . import order
            return order.Order(jsondict, strict=strict)
        if "OrderResponse" == resource_name:
            from . import orderresponse
            return orderresponse.OrderResponse(jsondict, strict=strict)
        if "OrderWhen" == resource_name:
            from . import order
            return order.OrderWhen(jsondict, strict=strict)
        if "Organization" == resource_name:
            from . import organization
            return organization.Organization(jsondict, strict=strict)
        if "OrganizationContact" == resource_name:
            from . import organization
            return organization.OrganizationContact(jsondict, strict=strict)
        if "Parameters" == resource_name:
            from . import parameters
            return parameters.Parameters(jsondict, strict=strict)
        if "ParametersParameter" == resource_name:
            from . import parameters
            return parameters.ParametersParameter(jsondict, strict=strict)
        if "Patient" == resource_name:
            from . import patient
            return patient.Patient(jsondict, strict=strict)
        if "PatientAnimal" == resource_name:
            from . import patient
            return patient.PatientAnimal(jsondict, strict=strict)
        if "PatientCommunication" == resource_name:
            from . import patient
            return patient.PatientCommunication(jsondict, strict=strict)
        if "PatientContact" == resource_name:
            from . import patient
            return patient.PatientContact(jsondict, strict=strict)
        if "PatientLink" == resource_name:
            from . import patient
            return patient.PatientLink(jsondict, strict=strict)
        if "PaymentNotice" == resource_name:
            from . import paymentnotice
            return paymentnotice.PaymentNotice(jsondict, strict=strict)
        if "PaymentReconciliation" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict, strict=strict)
        if "PaymentReconciliationDetail" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict, strict=strict)
        if "PaymentReconciliationNote" == resource_name:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationNote(jsondict, strict=strict)
        if "Period" == resource_name:
            from . import period
            return period.Period(jsondict, strict=strict)
        if "Person" == resource_name:
            from . import person
            return person.Person(jsondict, strict=strict)
        if "PersonLink" == resource_name:
            from . import person
            return person.PersonLink(jsondict, strict=strict)
        if "Practitioner" == resource_name:
            from . import practitioner
            return practitioner.Practitioner(jsondict, strict=strict)
        if "PractitionerPractitionerRole" == resource_name:
            from . import practitioner
            return practitioner.PractitionerPractitionerRole(jsondict, strict=strict)
        if "PractitionerQualification" == resource_name:
            from . import practitioner
            return practitioner.PractitionerQualification(jsondict, strict=strict)
        if "Procedure" == resource_name:
            from . import procedure
            return procedure.Procedure(jsondict, strict=strict)
        if "ProcedureFocalDevice" == resource_name:
            from . import procedure
            return procedure.ProcedureFocalDevice(jsondict, strict=strict)
        if "ProcedurePerformer" == resource_name:
            from . import procedure
            return procedure.ProcedurePerformer(jsondict, strict=strict)
        if "ProcedureRequest" == resource_name:
            from . import procedurerequest
            return procedurerequest.ProcedureRequest(jsondict, strict=strict)
        if "ProcessRequest" == resource_name:
            from . import processrequest
            return processrequest.ProcessRequest(jsondict, strict=strict)
        if "ProcessRequestItem" == resource_name:
            from . import processrequest
            return processrequest.ProcessRequestItem(jsondict, strict=strict)
        if "ProcessResponse" == resource_name:
            from . import processresponse
            return processresponse.ProcessResponse(jsondict, strict=strict)
        if "ProcessResponseNotes" == resource_name:
            from . import processresponse
            return processresponse.ProcessResponseNotes(jsondict, strict=strict)
        if "Provenance" == resource_name:
            from . import provenance
            return provenance.Provenance(jsondict, strict=strict)
        if "ProvenanceAgent" == resource_name:
            from . import provenance
            return provenance.ProvenanceAgent(jsondict, strict=strict)
        if "ProvenanceAgentRelatedAgent" == resource_name:
            from . import provenance
            return provenance.ProvenanceAgentRelatedAgent(jsondict, strict=strict)
        if "ProvenanceEntity" == resource_name:
            from . import provenance
            return provenance.ProvenanceEntity(jsondict, strict=strict)
        if "Quantity" == resource_name:
            from . import quantity
            return quantity.Quantity(jsondict, strict=strict)
        if "Questionnaire" == resource_name:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict, strict=strict)
        if "QuestionnaireGroup" == resource_name:
            from . import questionnaire
            return questionnaire.QuestionnaireGroup(jsondict, strict=strict)
        if "QuestionnaireGroupQuestion" == resource_name:
            from . import questionnaire
            return questionnaire.QuestionnaireGroupQuestion(jsondict, strict=strict)
        if "QuestionnaireResponse" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict, strict=strict)
        if "QuestionnaireResponseGroup" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseGroup(jsondict, strict=strict)
        if "QuestionnaireResponseGroupQuestion" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseGroupQuestion(jsondict, strict=strict)
        if "QuestionnaireResponseGroupQuestionAnswer" == resource_name:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseGroupQuestionAnswer(jsondict, strict=strict)
        if "Range" == resource_name:
            from . import range
            return range.Range(jsondict, strict=strict)
        if "Ratio" == resource_name:
            from . import ratio
            return ratio.Ratio(jsondict, strict=strict)
        if "Reference" == resource_name:
            from . import reference
            return reference.Reference(jsondict, strict=strict)
        if "ReferralRequest" == resource_name:
            from . import referralrequest
            return referralrequest.ReferralRequest(jsondict, strict=strict)
        if "RelatedPerson" == resource_name:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict, strict=strict)
        if "Resource" == resource_name:
            from . import resource
            return resource.Resource(jsondict, strict=strict)
        if "RiskAssessment" == resource_name:
            from . import riskassessment
            return riskassessment.RiskAssessment(jsondict, strict=strict)
        if "RiskAssessmentPrediction" == resource_name:
            from . import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict, strict=strict)
        if "SampledData" == resource_name:
            from . import sampleddata
            return sampleddata.SampledData(jsondict, strict=strict)
        if "Schedule" == resource_name:
            from . import schedule
            return schedule.Schedule(jsondict, strict=strict)
        if "SearchParameter" == resource_name:
            from . import searchparameter
            return searchparameter.SearchParameter(jsondict, strict=strict)
        if "SearchParameterContact" == resource_name:
            from . import searchparameter
            return searchparameter.SearchParameterContact(jsondict, strict=strict)
        if "Signature" == resource_name:
            from . import signature
            return signature.Signature(jsondict, strict=strict)
        if "Slot" == resource_name:
            from . import slot
            return slot.Slot(jsondict, strict=strict)
        if "Specimen" == resource_name:
            from . import specimen
            return specimen.Specimen(jsondict, strict=strict)
        if "SpecimenCollection" == resource_name:
            from . import specimen
            return specimen.SpecimenCollection(jsondict, strict=strict)
        if "SpecimenContainer" == resource_name:
            from . import specimen
            return specimen.SpecimenContainer(jsondict, strict=strict)
        if "SpecimenTreatment" == resource_name:
            from . import specimen
            return specimen.SpecimenTreatment(jsondict, strict=strict)
        if "StructureDefinition" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict, strict=strict)
        if "StructureDefinitionContact" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionContact(jsondict, strict=strict)
        if "StructureDefinitionDifferential" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict, strict=strict)
        if "StructureDefinitionMapping" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict, strict=strict)
        if "StructureDefinitionSnapshot" == resource_name:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict, strict=strict)
        if "Subscription" == resource_name:
            from . import subscription
            return subscription.Subscription(jsondict, strict=strict)
        if "SubscriptionChannel" == resource_name:
            from . import subscription
            return subscription.SubscriptionChannel(jsondict, strict=strict)
        if "Substance" == resource_name:
            from . import substance
            return substance.Substance(jsondict, strict=strict)
        if "SubstanceIngredient" == resource_name:
            from . import substance
            return substance.SubstanceIngredient(jsondict, strict=strict)
        if "SubstanceInstance" == resource_name:
            from . import substance
            return substance.SubstanceInstance(jsondict, strict=strict)
        if "SupplyDelivery" == resource_name:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict, strict=strict)
        if "SupplyRequest" == resource_name:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict, strict=strict)
        if "SupplyRequestWhen" == resource_name:
            from . import supplyrequest
            return supplyrequest.SupplyRequestWhen(jsondict, strict=strict)
        if "TestScript" == resource_name:
            from . import testscript
            return testscript.TestScript(jsondict, strict=strict)
        if "TestScriptContact" == resource_name:
            from . import testscript
            return testscript.TestScriptContact(jsondict, strict=strict)
        if "TestScriptFixture" == resource_name:
            from . import testscript
            return testscript.TestScriptFixture(jsondict, strict=strict)
        if "TestScriptMetadata" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadata(jsondict, strict=strict)
        if "TestScriptMetadataCapability" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadataCapability(jsondict, strict=strict)
        if "TestScriptMetadataLink" == resource_name:
            from . import testscript
            return testscript.TestScriptMetadataLink(jsondict, strict=strict)
        if "TestScriptSetup" == resource_name:
            from . import testscript
            return testscript.TestScriptSetup(jsondict, strict=strict)
        if "TestScriptSetupAction" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict, strict=strict)
        if "TestScriptSetupActionAssert" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict, strict=strict)
        if "TestScriptSetupActionOperation" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionOperation(jsondict, strict=strict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_name:
            from . import testscript
            return testscript.TestScriptSetupActionOperationRequestHeader(jsondict, strict=strict)
        if "TestScriptTeardown" == resource_name:
            from . import testscript
            return testscript.TestScriptTeardown(jsondict, strict=strict)
        if "TestScriptTeardownAction" == resource_name:
            from . import testscript
            return testscript.TestScriptTeardownAction(jsondict, strict=strict)
        if "TestScriptTest" == resource_name:
            from . import testscript
            return testscript.TestScriptTest(jsondict, strict=strict)
        if "TestScriptTestAction" == resource_name:
            from . import testscript
            return testscript.TestScriptTestAction(jsondict, strict=strict)
        if "TestScriptVariable" == resource_name:
            from . import testscript
            return testscript.TestScriptVariable(jsondict, strict=strict)
        if "Timing" == resource_name:
            from . import timing
            return timing.Timing(jsondict, strict=strict)
        if "TimingRepeat" == resource_name:
            from . import timing
            return timing.TimingRepeat(jsondict, strict=strict)
        if "ValueSet" == resource_name:
            from . import valueset
            return valueset.ValueSet(jsondict, strict=strict)
        if "ValueSetCodeSystem" == resource_name:
            from . import valueset
            return valueset.ValueSetCodeSystem(jsondict, strict=strict)
        if "ValueSetCodeSystemConcept" == resource_name:
            from . import valueset
            return valueset.ValueSetCodeSystemConcept(jsondict, strict=strict)
        if "ValueSetCodeSystemConceptDesignation" == resource_name:
            from . import valueset
            return valueset.ValueSetCodeSystemConceptDesignation(jsondict, strict=strict)
        if "ValueSetCompose" == resource_name:
            from . import valueset
            return valueset.ValueSetCompose(jsondict, strict=strict)
        if "ValueSetComposeInclude" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeInclude(jsondict, strict=strict)
        if "ValueSetComposeIncludeConcept" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict, strict=strict)
        if "ValueSetComposeIncludeFilter" == resource_name:
            from . import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict, strict=strict)
        if "ValueSetContact" == resource_name:
            from . import valueset
            return valueset.ValueSetContact(jsondict, strict=strict)
        if "ValueSetExpansion" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansion(jsondict, strict=strict)
        if "ValueSetExpansionContains" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansionContains(jsondict, strict=strict)
        if "ValueSetExpansionParameter" == resource_name:
            from . import valueset
            return valueset.ValueSetExpansionParameter(jsondict, strict=strict)
        if "VisionPrescription" == resource_name:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict, strict=strict)
        if "VisionPrescriptionDispense" == resource_name:
            from . import visionprescription
            return visionprescription.VisionPrescriptionDispense(jsondict, strict=strict)
        from . import element
        return element.Element(jsondict, strict=strict)
